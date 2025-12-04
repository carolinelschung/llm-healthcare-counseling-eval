# Metrics Explained

This document defines the metrics used and summarizes how to interpret the
model outputs.

---

## 1. Readability

### **Flesch Reading Ease**
- Scale: 0–100  
- Higher = easier to understand  

Example scores observed in the study:

- **~50** (GPT-4.1-mini): easy-to-moderate reading difficulty  
- **~34** (Claude): more complex, academic tone  

---

## 2. Sentiment Score

A transformer-based model evaluates tone:

- **Positive** (supportive)  
- **Neutral** (informational)  
- **Negative** (discouraging or unclear)  

Scores observed:

- Range: **1.88–1.97**  
- All models leaned supportive, with Claude highest.

---

## 3. Fairness Score

Measures whether the LLM avoids:

- Blame  
- Judgment  
- Unequal framing  

Scores:

- Range: **0.66–1.35**  
- GPT-4.1-mini demonstrated the most consistently fair framing.

---

## 4. Stance Neutrality

A model predicting whether responses remain:

- Neutral  
- Overconfident  
- Opinionated  

Scores:

- Llama & GPT: **0.75**  
- Claude: **0.15**  
- Gemini: **-1.66** (least neutral)

---

## 5. Factuality Score

Lightweight factuality model evaluating likelihood that statements adhere to
general medical consensus.

Results:

- All models scored **between 3.74 and 3.82**, indicating similar accuracy.

---

## Aggregate Model Comparison

| Metric ↓ | Llama-70B | Gemini Flash | GPT-4.1-mini | Claude 3.7 Sonnet |
|----------|-----------|--------------|---------------|--------------------|
| **Flesch Reading Ease ↑** | 46.6 | 45.77 | **49.43** | 34.27 |
| **Sentiment ↑** | 1.96 | 1.88 | 1.90 | **1.97** |
| **Fairness ↑** | 0.66 | 0.71 | **1.35** | 0.79 |
| **Stance Neutrality ↑** | **0.75** | -1.66 | **0.75** | 0.15 |
| **Factuality ↑** | 3.74 | **3.81** | 3.76 | **3.82** |
