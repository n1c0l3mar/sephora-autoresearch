# Week 6: Iteration, Ablation, and Scope Lock

## Revised Project Statement
This project uses an AutoResearch loop to predict Sephora product ratings from structured product metadata. The final direction is focused on feature representation rather than broad model exploration. After repeated Random Forest tuning plateaued, adding `brand_name` back as a categorical predictor produced the best improvement, reducing validation MAE from 0.3284 to 0.3225.

The project’s contribution is a reproducible AutoResearch loop showing that better feature representation mattered more than model-only hyperparameter tuning for these predictions.

## Current Best Direction

I am committing to a feature-representation story: the model improved most when meaningful product metadata was included in the feature set. The final model direction is a Random Forest using the improved feature set.

## Supporting Evidence

| Direction Tested | Best Validation MAE | Decision | What It Showed |
|---|---:|---|---|
| Linear regression baseline | 0.3825 | Baseline | Starting benchmark |
| Random Forest model-only tuning | 0.3284 | Keep | Random Forest substantially improved over baseline |
| `max_features` tuning | ~0.329–0.330 | Discard | Did not meaningfully improve the model |
| `min_samples_leaf` increases | 0.3347–0.3520 | Discard | Larger leaves caused underfitting and worsened MAE |
| Week 5 model-only autonomous block | 0.3289 best run | Discard | Additional model-only changes plateaued |
| Add `brand_name` as categorical predictor | 0.3225 | Keep | Brand-level metadata gave the clearest improvement |
| Post-feature-engineering model tuning | 0.3226 best run | Discard | Additional tuning did not beat the feature-inclusion result |