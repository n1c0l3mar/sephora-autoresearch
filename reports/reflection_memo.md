# Reflection Memo

## What Worked Well

The AutoResearch framework successfully allowed experimentation on the Sephora rating prediction problem. The use of a fixed evaluation metric (validation MAE) and a fixed train/validation/test split made experiments comparable/reproducable across runs. Random Forest models consistently outperformed the baseline linear regression model, and feature engineering further improved performance.

## What Worked Poorly

Many hyperparameter tuning experiments produced little improvement over the current best model. Several model changes resulted in diminishing returns, suggesting that model selection alone was not sufficient to achieve large gains. 

## Lessons Learned

The project demonstrated that feature engineering often produced larger gains than extensive hyperparameter tuning. Maintaining a fixed evaluation pipeline was critical for ensuring valid comparisons between experiments.