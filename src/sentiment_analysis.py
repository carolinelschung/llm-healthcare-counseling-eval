"""
sentiment_analysis.py

Statistical comparison of sentiment scores across models using the
Friedman test, plus simple visualizations.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import friedmanchisquare
import seaborn as sns


def run_friedman_test(
    df: pd.DataFrame,
    score_columns: list[str],
) -> tuple[float, float]:
    """
    Run the Friedman test across the given numeric columns.

    Returns (statistic, p_value).
    """
    # Drop rows with any NaN in the relevant columns
    df_clean = df.dropna(subset=score_columns)

    stats_args = [df_clean[col] for col in score_columns]
    statistic, p_value = friedmanchisquare(*stats_args)
    return statistic, p_value


def sentiment_boxplot(
    df: pd.DataFrame,
    score_columns: list[str],
    title: str = "Sentiment score distribution by model",
) -> None:
    """
    Draw a boxplot comparing sentiment score distributions across models.
    """
    data = df[score_columns].melt(var_name="Model", value_name="Score")
    sns.boxplot(data=data, x="Model", y="Score")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main(
    input_path: str = "data/processed/healthcare_advice_with_scores.csv",
):
    df = pd.read_csv(input_path)

    # Example: auto-detect columns that look like sentiment scores
    score_cols = [
        c for c in df.columns
        if "Sentiment Score" in c
    ]

    print("Using score columns:", score_cols)

    stat, p = run_friedman_test(df, score_cols)
    print(f"Friedman statistic: {stat:.4f}, p-value: {p:.4e}")

    sentiment_boxplot(df, score_cols)


if __name__ == "__main__":
    main()
