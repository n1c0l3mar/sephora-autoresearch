# Week 4 Controlled Experiment Plan

## Goal

Test whether changing the `max_features` hyperparameter in `RandomForestRegressor` affects validation MAE.

## Experiment Axis

The experiment axis is `max_features`.

## Conditions

| Condition | max_features |
|---|---:|
| A | 0.5 |
| B | 0.7 |
| C | 1.0 |

## Held Fixed

- Model family: RandomForestRegressor
- n_estimators: 300
- min_samples_leaf: 1
- random_state: 390
- n_jobs: -1
- Preprocessing: unchanged
- Data split: unchanged
- Metric: validation MAE
- Evaluator: run.py
- Editable file: model.py only

## Success/Decision Rule

- keep: valid MAE lower than previous best
- discard: valid MAE greater than or equal to previous best
- crash: no valid MAE produced