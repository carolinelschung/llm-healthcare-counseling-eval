# Data Overview

This project evaluates LLM-generated healthcare counseling responses.

The full dataset used for analysis is not included in this repository due to
privacy and content-sensitivity considerations.

Instead, the `sample_inputs/` directory contains a small synthetic dataset
(`healthcare_queries_sample.csv`) that matches the schema of the real data.

## Real Dataset Structure (for reference)

- `query_id`: Unique identifier
- `patient_query`: Text of patient-submitted healthcare question
- `category`: High-level topic classification
- `source`: Forum, FAQ, or article source type
- `submitted_at`: Date of original submission

## processed/
This folder stores intermediate outputs such as model responses and processed scores.
It is intentionally empty in the repository. Files generated during the pipeline
(e.g., LLM responses or sentiment/readability scores) are not committed to GitHub
to avoid storing sensitive or large data artifacts.

A `.gitkeep` file is included only to preserve the directory structure.

## How to Use Your Own Data

To run the full pipeline:
1. Place your dataset in this folder.
2. Ensure it matches the schema above.
3. Update file paths in the notebooks or scripts as needed.

No LLM-generated responses or sensitive medical content are included in this repo.
