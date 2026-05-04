# Week 4 Controlled Experiment 

## Goal

Test whether changing the `max_features` hyperparameter in `RandomForestRegressor` affects validation MAE.

## Experiment Axis

The experiment axis is `max_features`.

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

# Week 4 Experiment-Result Matrix

| Run | Condition | max_features | Val MAE | Runtime sec | Status | Decision | Interpretation |
|---|---|---:|---:|---:|---|---|---|
| A | Lower feature subsampling | 0.5 | 0.3294 | 72.1585 | success | discard | Worse than current best MAE 0.3284 |
| B | Current/baseline setting | 0.7 | 0.3289 | 116.7758 | success | discard | Best within controlled 300-tree set so far, but worse than current best MAE 0.3284 |
| C | Intermediate feature subsampling | 0.72 | 0.33 | 114.0266 | success | discard | Worse than current best MAE 0.3284 |
| D | Intermediate feature subsampling | 0.75 | 0.3293 | 94.0711 | success | discard | Worse than current best MAE 0.3284 |
| E | Intermediate feature subsampling | 0.78 | 0.3298 | 109.8493 | success | discard | Worse than current best MAE 0.3284 |
| F | Intermediate feature subsampling | 0.82 | 0.3292 | 85.5758 | success | discard | Worse than current best MAE 0.3284 |
| G | Higher feature subsampling | 0.85 | 0.3293 | 144.2035 | success | discard | Worse than current best MAE 0.3284 |
| H | Full feature availability | 1.0 | 0.3296 | 120.5494 | success | discard | Worse than current best MAE 0.3284 |
