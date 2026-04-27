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
- `product_info.csv`

---

## Target Variable
- `rating`

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
```python
random_state = 390

## Reproducible Instructions

Follow these steps to reproduce the baseline model and results.

### 1. Clone the repository

```bash
git clone https://github.com/n1c0l3mar/sephora-autoresearch/tree/main
cd sephora-autoresearch

### 2. Install required packages 

pip install pandas numpy scikit-learn

### 3. Ensure the dataset is available

Make sure the file product_info.csv is located in the root directory of the project.

If the dataset is not included in the repository, download it from:
https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews

### 4. Run the baseline model

Execute the following command:

python3 run.py "baseline linear regression"


### 5. Expected output

After running the command, the terminal should display output similar to:

Validation MAE: ~0.38
Runtime seconds: ~0.07

### 6. Verify experiment log

Open the file results.tsv. A new row should appear similar to:

baseline linear regression 0.3825 0.07