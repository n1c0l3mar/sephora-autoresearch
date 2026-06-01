# Final Results Summary

The baseline linear regression produced a validation MAE of `0.3825`. The best result was `0.3225`, achieved after adding `brand_name` as a categorical predictor to the Random Forest feature set.

| Experiment | Model | Validation MAE | Outcome |
|---|---|---:|---|
| Baseline linear regression | Linear Regression | 0.3825 | Keep |
| Ridge regression (`alpha=1`) | Ridge Regression | 0.3821 | Keep |
| Lasso regression (`alpha=0.01`) | Lasso Regression | 0.3806 | Keep |
| Random forest, 100 trees | Random Forest Regressor | 0.3311 | Keep |
| Random forest, 400 trees, `max_features=0.7` | Random Forest Regressor | 0.3284 | Keep |
| Gradient boosting | Gradient Boosting Regressor | 0.3520 | Discard |
| Extra Trees, 500 trees, `min_samples_leaf=2`, `max_features=0.7` | Extra Trees Regressor | 0.3337 | Discard |
| Random forest, 1000 trees, `max_features=0.7` | Random Forest Regressor | 0.3289 | Discard |
| Add `brand_name` as categorical predictor | Random Forest Regressor with engineered feature set | **0.3225** | **Keep** |
| Post-feature-engineering random forest, 600 trees, `max_features=0.7` | Random Forest Regressor with engineered feature set | 0.3226 | Discard |
| Intentional failure logging test | Failed setup validation run | NA | Crash |
| Intentional model failure logging test | Random Forest Regressor with invalid `n_estimators` | NA | Crash |

## Key Findings

The largest improvement came from switching from linear models to Random Forest, reducing validation MAE from `0.3825` to `0.3311`. Further Random Forest tuning improved the result to `0.3284`. The best overall improvement came from feature representation: adding `brand_name` as a categorical predictor reduced MAE again to `0.3225`.

Gradient Boosting, Extra Trees, larger leaf sizes, depth limits, and broader Random Forest hyperparameter sweeps did not beat the best model. The two logged crashes were intentional tests of failure logging rather than viable modeling approaches.

The experiments showed diminishing returns from model-only tuning. Repeated Random Forest variations stayed close to the best score without surpassing it, including a post-feature-engineering 600-tree run at `0.3226`. This suggests the final `0.3225` result is a stable local optimum under the fixed evaluation setup.
