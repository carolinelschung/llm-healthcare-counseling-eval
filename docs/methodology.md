# Methodology

This document outlines the workflow used to evaluate LLM responses to synthetic
healthcare questions.

---

## 1. Input Dataset

The dataset includes:

- 10 synthetic healthcare questions
- Categories such as general_symptom, medication, chronic_condition
- Metadata (source, submission date)

Stored at: data/sample_inputs/healthcare_queries_sample.csv

---

## 2. Response Generation

Each question is passed to an LLM using a consistent, safe prompt template.  
Models evaluated:

- meta-llama/Llama-3.3-70B-Instruct
- google_genai.gemini-2.0-flash-001
- openai/gpt-4.1-mini
- anthropic/claude-3.7-sonnet

Outputs are stored **locally only**, never committed to the repo.

---

## 3. Readability Metrics

Two metrics were computed:

### **Flesch Reading Ease**
Higher = easier to read.

### **Flesch-Kincaid Grade Level**
Lower = easier reading level.

Results summary:

- **GPT-4.1-mini** produced the clearest responses (FRE = 49.43).
- **Claude 3.7 Sonnet** was the most complex (FRE = 34.27).

---

## 4. Sentiment Analysis

A transformer-based doctor–patient sentiment classifier produced:

- Positive/Neutral/Negative tone
- A continuous sentiment score

Results summary:

- **Claude 3.7 Sonnet** achieved the highest avg sentiment (1.97).
- All models scored within a narrow positive range.

---

## 5. Fairness & Stance Neutrality

Two additional dimensions were evaluated:

### **Fairness Score**
Higher = less biased framing toward the patient.

- GPT-4.1-mini was highest at **1.35**.

### **Stance Neutrality**
Measures whether the model avoids taking an unwarranted position.

- Llama and GPT were most neutral (0.75).
- Gemini scored negatively (-1.66).

---

## 6. Factuality Scoring

A lightweight factuality model rated each answer from 1–5.

- **Claude 3.7 Sonnet achieved the highest factuality (3.82)**.
- All models were in a tight 3.7–3.8 band.

---

## 7. Visualization

Plots, tables, and aggregated charts are stored in: results/

No raw LLM text is included.