# Employee Retention Prediction — MLOps Project

An end-to-end MLOps project I built for **predicting employee attrition**. It showcases a production-style pipeline from data ingestion and validation through feature engineering, model training, evaluation, and deployment, using industry-standard tools and cloud services.

---

## What This Project Demonstrates

- **End-to-end pipeline**: Data ingestion → validation → transformation → training → evaluation → deployment  
- **Reproducible experiments** and versioned model packaging  
- **Model storage** and retrieval via S3-compatible storage  
- **Dockerized** prediction service for portable deployment  
- **CI/CD-ready** setup with GitHub Actions, Docker, and AWS  

---

## Tech Stack

| Area | Technology |
|------|------------|
| **Language** | Python |
| **Data store** | MongoDB (dataset and ingestion) |
| **Model / artifacts** | AWS S3 |
| **Orchestration & CI** | GitHub Actions, Docker |
| **Serving** | FastAPI (with `app.py`) in a container |

---

## Project Structure

```
├── src/                    # Core pipeline (components, config, utils, entities)
├── notebook/               # EDA, feature engineering, dataset (e.g. hr_data.csv)
├── app.py                  # Prediction API and demo UI
├── Dockerfile              # Container image for the service
├── config/                 # YAML configs and schema definitions
└── requirements.txt
```

---

## Quick Start (Local)

1. **Environment and dependencies**

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

2. **Environment variables** (MongoDB and AWS; adjust for your setup)

```powershell
# $env:MONGODB_URL = "mongodb+srv://<username>:<password>@..."
# $env:AWS_ACCESS_KEY_ID = "..."
# $env:AWS_SECRET_ACCESS_KEY = "..."
```

3. **Run the API locally**

```bash
python app.py
# Open http://localhost:5080 for the demo UI
```

---

## Running the Training Pipeline

The full training flow is orchestrated in `src/pipline/training_pipeline.py`. Modular components live under `src/components/` (ingestion, transformation, training, evaluation, pusher).

Run training locally:

```bash
python -m src.pipline.training_pipeline
```

---

## Docker & Deployment

**Build:**

```bash
docker build -t employee-retention-mlops:latest .
```

**Run locally:**

```bash
docker run -p 5080:5080 --env-file .env employee-retention-mlops:latest
```

The project is set up to push artifacts to S3 and to use GitHub Actions for CI/CD (see `Dockerfile` and workflow files in the repo).

---

## Model Registry & Cloud

Trained models are saved and pushed to S3 via `src/cloud_storage/aws_storage.py`. Credentials are intended to be supplied via environment variables or a secret manager in CI.

---

## Highlights to Review

1. **`notebook/exp-notebook.ipynb`** — EDA and feature engineering  
2. **`src/components/data_ingestion.py`** — Data fetch and storage  
3. **`src/components/model_trainer.py`** — Training loop and model persistence  
4. **`app.py`** — Prediction API and simple UI  

---

## Possible Extensions

- Automated tests and model monitoring  
- Experiment tracking (e.g. MLflow or Weights & Biases)  
- Production deployment (e.g. AWS ECS/EKS or serverless inference)  

---

## Contact

For a walkthrough, code review, or demo, feel free to open an issue or reach out.

Thanks for looking at this Employee Retention MLOps project — built to be extended into production-grade workflows.
