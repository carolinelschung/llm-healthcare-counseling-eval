"""
stance_visualization.py

Train a simple stance classifier on LLM responses using Doc2Vec
and classical ML models. 
"""

from __future__ import annotations

from typing import Tuple

import nltk
import pandas as pd
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def tokenize(text: str) -> list[str]:
    return nltk.word_tokenize(text.lower())


def build_doc2vec_embeddings(
    texts: list[str],
    vector_size: int = 100,
    min_count: int = 2,
    epochs: int = 20,
) -> Tuple[Doc2Vec, list[list[float]]]:
    tagged_docs = [
        TaggedDocument(words=tokenize(t), tags=[i]) for i, t in enumerate(texts)
    ]
    model = Doc2Vec(
        vector_size=vector_size,
        min_count=min_count,
        workers=4,
        epochs=epochs,
    )
    model.build_vocab(tagged_docs)
    model.train(tagged_docs, total_examples=model.corpus_count, epochs=model.epochs)

    vectors = [model.infer_vector(tokenize(t)) for t in texts]
    return model, vectors


def train_stance_classifier(
    df: pd.DataFrame,
    text_col: str = "ResponseText",
    label_col: str = "StanceLabel",
):
    texts = df[text_col].fillna("").tolist()
    labels = df[label_col].tolist()

    doc2vec_model, X = build_doc2vec_embeddings(texts)
    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, test_size=0.2, random_state=42, stratify=labels
    )

    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    return doc2vec_model, clf


def main(input_path: str = "data/processed/stance_labeled_responses.csv"):
    df = pd.read_csv(input_path)
    train_stance_classifier(df)


if __name__ == "__main__":
    main()
