# LLM Healthcare Counseling Evaluation Pipeline

This repository provides a modular, reproducible framework for evaluating how large language models (LLMs) respond to *synthetic* patient-style healthcare questions.  
The pipeline supports:

- **LLM response collection**
- **Readability scoring**
- **Sentiment + fairness analysis**
- **Stance neutrality evaluation**
- **Factuality scoring**
- **Visualization + summary metrics**

No sensitive or real user data is included. All examples use small, synthetic health-related questions for demonstration.

---

## Key Features

- **Modular Python pipeline** (collect → process → visualize)
- **Model-agnostic prompt evaluation**
- **Safe synthetic dataset**
- **Clear documentation and notebooks**
- **Automatic computation of:**
  - Flesch Reading Ease  
  - Flesch-Kincaid Grade Level  
  - Sentiment (Transformer-based)  
  - Fairness Score  
  - Stance Neutrality  
  - Factuality Score  
- **Plots + summary tables** ready for research reports or presentations

---

## Summary of Model Results

| Model | Reading Ease ↑ | Grade Level ↓ | Sentiment ↑ | Fairness ↑ | Stance Neutrality ↑ | Factuality ↑ |
|-------|----------------|----------------|--------------|-------------|----------------------|---------------|
| **meta-llama/Llama-3.3-70B-Instruct** | 46.6 | 45.23 | 1.96 | 0.66 | **0.75** | 3.74 |
| **google_genai.gemini-2.0-flash-001** | 45.77 | 46.1 | 1.88 | 0.71 | -1.66 | 3.81 |
| **openai/gpt-4.1-mini** | **49.43** | **49.78** | 1.90 | **1.35** | **0.75** | 3.76 |
| **anthropic/claude-3.7-sonnet** | 34.27 | 37.89 | **1.97** | 0.79 | 0.15 | **3.82** |

**Interpretation (high-level):**
- **GPT-4.1-mini** → clearest writing & fair framing  
- **Claude 3.7 Sonnet** → warmest/safest tone & highest factuality  
- **Llama 70B** → moderate clarity and neutrality  
- **Gemini Flash** → least neutral stance in this dataset  

---

## Pipeline Overview

The evaluation pipeline runs in three stages:

<p align="center">
  <img src="results/pipeline_flowchart.png" width="600">
</p>

---

## Repository Structure
```pgsql
llm-healthcare-counseling-eval/
│
├── data/
│ ├── sample_inputs/ # Synthetic healthcare questions
│ ├── processed/ # Generated responses + scored outputs (ignored in git)
│ └── schema.json # Machine-readable schema
│
├── docs/ # Full project documentation
│ ├── project_overview.md
│ ├── methodology.md
│ ├── metrics_explained.md
│ ├── data_schema.md
│ ├── api_usage.md
│ └── installation_guide.md
│
├── notebooks/ # Walkthrough notebooks
│ ├── 1_explore_input_data.ipynb
│ ├── 2_generate_llm_responses.ipynb
│ ├── 3_process_scores.ipynb
│ └── 4_visualize_outputs.ipynb
│
├── results/ # Safe, aggregate outputs
│ ├── pipeline_flowchart.png
│ ├── readability_by_model.png
│ ├── sentiment_scores_by_model.png
│ ├── political_bias_distribution.png (optional)
│ └── summary_metrics_table.csv
│
├── src/ # Source code
│ ├── collect_responses.py
│ └── process_responses.py
│
├── requirements.txt
└── README.md # (this file)
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd llm-healthcare-counseling-eval
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API key
Create a .env file:
DARTMOUTH_CHAT_API_KEY=your_key_here
This file is ignored by git for safety.

## Running the Pipeline

### 1. Generate model responses
```bash
python -m src.collect_responses
```

Output saved to:
```bash
data/processed/healthcare_advice_with_responses.csv
```
(This file is ignored in the repo.)

### 2. Process readability, sentiment, fairness, stance, and factuality
```bash
python -m src.process_responses
```
Output saved to data/processed/.

3. Visualize outputs
Open:
```bash
notebooks/4_visualize_outputs.ipynb
```

Visualizations exported to:
```bash
results/
```

## Documentation
| Topic                     | File                         |
| ------------------------- | ---------------------------- |
| Project overview          | `docs/project_overview.md`   |
| Methods used              | `docs/methodology.md`        |
| Explanation of metrics    | `docs/metrics_explained.md`  |
| Dataset schema            | `docs/data_schema.md`        |
| API configuration         | `docs/api_usage.md`          |
| Installation instructions | `docs/installation_guide.md` |

## Safety & Ethics
* No real patient data is used.
* All questions are synthetic.
* Raw LLM responses are never committed to GitHub.
* Only derived metrics and visualizations are included.

## Future Work
* Add more LLMs for comparison.
* Add hallucination detection.
* Expand fairness metrics.
* Provide a benchmarking dashboard.
