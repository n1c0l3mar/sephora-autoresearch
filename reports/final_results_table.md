# Final Results Table

| Experiment | Model / Direction | Validation MAE | Outcome |
|------------|-------------------|----------------|---------|
| Baseline | Linear Regression | 0.3825 | Baseline |
| Experiment 1 | Ridge Regression | 0.3821 | Discarded |
| Experiment 2 | Lasso Regression | 0.3806 | Discarded |
| Experiment 3 | Random Forest, 100 Trees | 0.3311 | Kept |
| Experiment 4 | Gradient Boosting | 0.3520 | Discarded |
| Failed Direction | HistGradientBoosting | N/A | Crash |
| Best Final Candidate | Feature-Engineered Random Forest | 0.3225 | Final Best |

## Conclusion

Random Forest achieved the best validation performance and was selected as the final model.