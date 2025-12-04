"""
factuality_analysis.py

Analyze factuality scores across models and visualize distributions.
"""

from __future__ import annotations

import re

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def extract_model_name(col: str) -> str:
    """
    Given a column like 'Factuality on GPT-4', extract 'GPT-4'.
    Adjust regex to match your actual column naming.
    """
    match = re.search(r"factuality on (.+)", col, re.IGNORECASE)
    return match.group(1) if match else col


def melt_factuality_columns(df: pd.DataFrame) -> pd.DataFrame:
    fact_cols = [c for c in df.columns if "factuality" in c.lower()]
    melted = df[fact_cols].melt(var_name="RawModelCol", value_name="Factuality")
    melted["Model"] = melted["RawModelCol"].apply(extract_model_name)
    return melted


def plot_factuality_distribution(melted: pd.DataFrame) -> None:
    sns.boxplot(data=melted, x="Model", y="Factuality")
    plt.title("Factuality score by model")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main(input_path: str = "data/processed/healthcare_advice_with_scores.csv"):
    df = pd.read_csv(input_path)
    melted = melt_factuality_columns(df)
    plot_factuality_distribution(melted)


if __name__ == "__main__":
    main()
