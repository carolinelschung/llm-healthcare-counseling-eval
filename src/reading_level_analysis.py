"""
reading_level_analysis.py

Compare reading-level scores across models using stats & plots.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import friedmanchisquare
import seaborn as sns


def run_friedman_on_readability(
    df: pd.DataFrame,
    readability_cols: list[str],
):
    df_clean = df.dropna(subset=readability_cols)
    args = [df_clean[col] for col in readability_cols]
    return friedmanchisquare(*args)


def readability_boxplot(
    df: pd.DataFrame,
    readability_cols: list[str],
    title: str = "Reading ease by model",
) -> None:
    data = df[readability_cols].melt(var_name="Model", value_name="ReadingEase")
    sns.boxplot(data=data, x="Model", y="ReadingEase")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main(
    input_path: str = "data/processed/healthcare_advice_with_scores.csv",
):
    df = pd.read_csv(input_path)

    # Example: pick columns that look like Flesch scores
    readability_cols = [
        c for c in df.columns
        if c.endswith(" - Flesch")
    ]

    print("Using readability columns:", readability_cols)
    stat, p = run_friedman_on_readability(df, readability_cols)
    print(f"Friedman statistic: {stat:.4f}, p-value: {p:.4e}")

    readability_boxplot(df, readability_cols)


if __name__ == "__main__":
    main()
