# Sephora Rating Prediction — AutoResearch Project

## Project Title
Predicting Sephora Product Ratings Using Structured Product Data

---

## Week 2 Goal
Establish a fully reproducible baseline model with a fixed evaluation pipeline that can be run end-to-end.

---

## Research Question
Which structured product features (e.g., price, category, product metadata) best predict Sephora product ratings?

---

## Data Source
Kaggle Dataset:  
https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews  

This project uses:
- product_info.csv

---

## Target Variable
- rating

---

## Validation Metric
- Mean Absolute Error (MAE)

Lower MAE = better model

---

## Train / Validation / Test Split
- Train: 70%
- Validation: 15%
- Test: 15%

Deterministic split using:

random_state = 390

---

## Reproducible Instructions

Follow these steps to reproduce the baseline model and results.

### 1. Clone the repository

git clone https://github.com/n1c0l3mar/sephora-autoresearch  
cd sephora-autoresearch  

---

### 2. Install required packages 

pip install pandas numpy scikit-learn  

---

### 3. Ensure the dataset is available

Make sure the file product_info.csv is located in the root directory of the project.

If the dataset is not included in the repository, download it from:  
https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews  

---

### 4. Run the baseline model

python3 run.py "baseline linear regression"  

---

### 5. Expected output

After running the command, the terminal should display output similar to:

Validation MAE: ~0.38  
Runtime seconds: ~0.07  

---

### 6. Verify experiment log

Open the file results.tsv. A new row should appear similar to:

baseline linear regression    0.3825    0.07  

## Failure Modes

The following failure patterns were observed during experimentation:

- Incorrect Imports  
  Some models failed due to importing from the wrong sklearn module.

- Model Compatibility Issues  
  Certain models (e.g., HistGradientBoosting) failed due to incompatibility with preprocessing or data format.

- Runtime Failures  
  Some experiments crashed and did not produce a valid MAE, so they were not logged in `results.tsv`.

- Logging Limitation  
  Failed runs are not automatically recorded in `results.tsv`, so failures must be tracked manually.