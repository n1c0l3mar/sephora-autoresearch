# Sephora AutoResearch Project
This project predicts Sephora product ratings using structured product data.  
The goal is to build an AutoResearch pipeline that iteratively improves model performance using a fixed evaluation metric (MAE).

## Problem
Predict product ratings for Sephora products using structured product features data.

## Data
[Kaggle Sephora Products Information](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews?select=product_info.csv)

This project uses the structured product dataset (~8,500 products, 27 features).  
The target variable is product rating.

## Metric
Mean Absolute Error (MAE)

## Baseline & Current Result
A simple regression model predicting ratings from product features.

- Model: Linear Regression
- Validation Metric: Mean Absolute Error (MAE)
- Validation MAE: 0.3825
- Runtime: ~0.07 seconds

This baseline serves as the benchmark for future improvements.

## How to Run
1. Open the Google Colab notebook: `Sephora_baseline.ipynb`
2. Run all cells from top to bottom
3. The notebook will:
   - Load the dataset
   - Train a baseline model
   - Output validation MAE and runtime

## Goal
Improve MAE through iterative model changes using an AutoResearch loop.

## Next Steps

- Test more complex models (Random Forest, Gradient Boosting)
- Improve feature engineering
- Implement AutoResearch-style iteration loop
