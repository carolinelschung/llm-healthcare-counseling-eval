"""
collect_responses.py

Query LLMs via Dartmouth Cloud for a dataset of healthcare advice queries
and save model responses to disk.
"""

from __future__ import annotations

import os
from typing import Iterable, List, Dict

import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm

from langchain_dartmouth.llms import ChatDartmouthCloud

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

load_dotenv()

DARTMOUTH_CHAT_API_KEY = os.getenv("DARTMOUTH_CHAT_API_KEY")

if DARTMOUTH_CHAT_API_KEY is None:
    raise RuntimeError(
        "DARTMOUTH_CHAT_API_KEY is not set. "
        "Add it to your environment or a .env file."
    )

TEMPERATURE: float = 0.7
MAX_TOKENS: int = 750

# Update this list to whatever models you actually want to query
MODELS_TO_QUERY: List[str] = [
    "meta-llama/Llama-3.3-70B-Instruct",
    # "openai/gpt-4.1-mini",
    # "anthropic/claude-3.7-sonnet",
]


# ---------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------

def query_dartmouth(
    prompt: str | List[Dict[str, str]],
    model_name: str,
    temperature: float = TEMPERATURE,
    max_tokens: int = MAX_TOKENS,
) -> str:
    """Query a single model on Dartmouth Cloud."""
    if isinstance(prompt, list):
        prompt_text = "\n".join([p["content"] for p in prompt])
    else:
        prompt_text = prompt

    llm = ChatDartmouthCloud(
        model_name=model_name,
        temperature=temperature,
        dartmouth_chat_api_key=DARTMOUTH_CHAT_API_KEY,
        max_tokens=max_tokens,
    )

    response = llm.invoke(prompt_text)
    return response.content


def build_prompt_from_row(row: pd.Series) -> str:
    """
    Build the prompt using your CSV schema:

    - patient_query        (main text)
    - category             (optional extra context)
    - source, submitted_at (optionally mentioned)
    """
    question = str(row["patient_query"]).strip()

    extras = []
    if "category" in row and isinstance(row["category"], str) and row["category"].strip():
        extras.append(f"Topic: {row['category'].strip()}")

    if "source" in row and isinstance(row["source"], str) and row["source"].strip():
        extras.append(f"Source type: {row['source'].strip()}")

    header = "A patient is asking for healthcare advice.\n"
    body = f"Patient question: {question}"

    context = ""
    if extras:
        context = "\n" + "\n".join(extras)

    instructions = (
        "\n\nPlease provide a clear, helpful, and safe response. "
        "Use plain language that a layperson can understand, and avoid giving "
        "specific diagnoses or treatment plans without advising the patient "
        "to consult a qualified healthcare professional."
    )

    return header + body + context + instructions


def generate_responses_for_models(
    df: pd.DataFrame,
    models: Iterable[str] = MODELS_TO_QUERY,
    prompt_col: str = "full_prompt",
) -> pd.DataFrame:
    """
    Given a DataFrame with the healthcare queries, build prompts and
    query each model. Adds one `<model> response` column per model.
    """
    # Build prompts if not already present
    if prompt_col not in df.columns:
        df[prompt_col] = df.apply(build_prompt_from_row, axis=1)

    for model in models:
        responses: list[str] = []
        print(f"Querying model: {model}")

        for _, row in tqdm(df.iterrows(), total=len(df)):
            prompt_text = row[prompt_col]
            try:
                response = query_dartmouth(
                    prompt_text,
                    model_name=model,
                    temperature=TEMPERATURE,
                    max_tokens=MAX_TOKENS,
                )
            except Exception as e:
                response = f"[Error]: {e}"
            responses.append(response)

        df[f"{model} response"] = responses

    return df


def main(
    input_path: str = "data/sample_inputs/healthcare_queries_sample.csv",
    output_path: str = "data/processed/healthcare_advice_with_responses.csv",
) -> None:
    """
    High-level entrypoint: load your sample CSV, query models,
    and save responses.
    """
    df = pd.read_csv(input_path)
    df = generate_responses_for_models(df)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved responses to {output_path}")


if __name__ == "__main__":
    main()
