# Project Overview

This repository presents a reproducible evaluation pipeline for analyzing how
large language models (LLMs) respond to patient-style healthcare questions.  
The pipeline demonstrates how to:

- Generate model responses using a standardized prompt format.
- Compute readability, sentiment, fairness, stance neutrality, and factuality.
- Produce aggregated, model-level comparison metrics.
- Visualize results without storing any sensitive model outputs.

Only **synthetic healthcare questions** are used, and no patient data of any kind
is included.

---

## Goals

The project is designed to:

- Evaluate how clearly different LLMs communicate basic health information.
- Compare tone, clarity, and neutrality across models.
- Demonstrate modular components for data collection, scoring, and visualization.
- Provide a safe, research-ready workflow for LLM evaluation.

---

## Models Evaluated

The following four models were evaluated:

- **meta-llama/Llama-3.3-70B-Instruct**
- **google_genai.gemini-2.0-flash-001**
- **openai/gpt-4.1-mini**
- **anthropic/claude-3.7-sonnet**

---

## Results Summary

| Model | Avg Flesch Reading Ease ↑ | Avg Grade Level ↓ | Avg Sentiment ↑ | Avg Fairness ↑ | Neutral Stance % ↑ | Avg Factuality ↑ |
|-------|----------------------------|--------------------|------------------|-----------------|---------------------|-------------------|
| Llama-3.3-70B | **46.6** | **45.23** | **1.96** | 0.66 | **0.75** | 3.74 |
| Gemini 2.0 Flash | 45.77 | 46.1 | 1.88 | 0.71 | -1.66 | 3.81 |
| GPT-4.1-mini | **49.43** | **49.78** | 1.90 | **1.35** | **0.75** | 3.76 |
| Claude 3.7 Sonnet | 34.27 | 37.89 | **1.97** | **0.79** | 0.15 | **3.82** |

Key takeaways:

- **GPT-4.1-mini** produced the **easiest-to-read** responses.
- **Claude 3.7 Sonnet** showed the **strongest sentiment (supportiveness)**.
- **GPT-4.1-mini** led in **fairness**.
- **Gemini Flash** scored lowest on stance neutrality.
- **Claude 3.7 Sonnet** had the **highest factuality score**.

Full explanations of each metric appear in `metrics_explained.md`.

---

## Pipeline Diagram

Include your exported pipeline figure here:

<p align="center">
  <img src="../results/pipeline_flowchart.png" width="600">
</p>
