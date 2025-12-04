"""
process_responses.py

Readability and sentiment processing for LLM-generated healthcare responses.
"""

from __future__ import annotations

from typing import List

import pandas as pd
import textstat
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


# ---------------------------------------------------------------------
# Readability
# ---------------------------------------------------------------------

def add_readability_scores(
    df: pd.DataFrame,
    response_columns: List[str],
    prefix: str = "Flesch",
) -> pd.DataFrame:
    """
    Adds readability scores for each column in response_columns.

    For each column `col`, creates:
    - f"{col} - {prefix}" : Flesch score (float or None)
    - f"{col} - {prefix} Grade" : Flesch-Kincaid grade level (float or None)
    """
    for col in response_columns:
        text_series = df[col].fillna("")

        df[f"{col} - {prefix}"] = text_series.apply(
            lambda x: textstat.flesch_reading_ease(x)
            if isinstance(x, str) and x and not str(x).startswith("[Error]")
            else None
        )

        df[f"{col} - {prefix} Grade"] = text_series.apply(
            lambda x: textstat.flesch_kincaid_grade(x)
            if isinstance(x, str) and x and not str(x).startswith("[Error]")
            else None
        )

    return df


# ---------------------------------------------------------------------
# Sentiment (doctor–patient style)
# ---------------------------------------------------------------------

def build_sentiment_pipeline(
    model_name: str = "DrishtiSharma/BERT-Base-Uncased_for-Doctor-Patient-Sentiment",
):
    """
    Builds a transformers sentiment pipeline. Adjust the model name to match
    what you actually used.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


def add_sentiment_scores(
    df: pd.DataFrame,
    response_columns: List[str],
    sentiment_pipe=None,
    score_prefix: str = "Sentiment",
) -> pd.DataFrame:
    """
    Adds sentiment labels & scores for each response column.

    For each col, creates:
    - f"{col} - {score_prefix} Label"
    - f"{col} - {score_prefix} Score"
    """
    if sentiment_pipe is None:
        sentiment_pipe = build_sentiment_pipeline()

    for col in response_columns:
        labels = []
        scores = []
        for text in df[col].fillna(""):
            if not isinstance(text, str) or not text or text.startswith("[Error]"):
                labels.append(None)
                scores.append(None)
                continue

            result = sentiment_pipe(text)[0]
            labels.append(result.get("label"))
            scores.append(result.get("score"))

        df[f"{col} - {score_prefix} Label"] = labels
        df[f"{col} - {score_prefix} Score"] = scores

    return df


def main(
    input_path: str = "data/processed/healthcare_advice_with_responses.csv",
    output_path: str = "data/processed/healthcare_advice_with_scores.csv",
) -> None:
    """
    Load responses, compute readability + sentiment, and save augmented CSV.
    """
    df = pd.read_csv(input_path)

    # Update this list to your actual response column names
    response_cols = [
        col for col in df.columns
        if col.endswith("response")
    ]

    df = add_readability_scores(df, response_cols)
    df = add_sentiment_scores(df, response_cols)

    df.to_csv(output_path, index=False)
    print(f"Saved processed data to {output_path}")


if __name__ == "__main__":
    main()
