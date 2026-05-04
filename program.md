# AutoResearch Program: Sephora Rating Prediction

## Objective
Improve prediction of Sephora product ratings by minimizing validation MAE.

## Data
The project uses `product_info.csv`, which contains structured product-level Sephora data.

## Target
The target variable is `rating`.

## Metric
The fixed validation metric is Mean Absolute Error (MAE). Lower MAE is better.

## Editable File
The agent may only modify:

- `model.py`

The agent may change:
- model type
- model hyperparameters
- model pipeline steps inside `build_model()`

## Frozen Files
The agent must not modify:

- `prepare.py`
- `run.py`
- `product_info.csv`
- `results.tsv` manually

## Keep / Discard / Crash Rule

Each experiment is evaluated using validation MAE.

- **Keep:** If the new model produces a lower validation MAE than the current best result, the model is kept as the new best version.
- **Discard:** If the new model produces a higher or equal validation MAE than the current best result, the model is discarded and not considered an improvement.
- **Crash:** If the experiment fails to run, produces an error, or does not return a valid MAE, it is considered a crash and is not treated as a valid result.

The current best model is determined based on the lowest validation MAE recorded in `results.tsv`.

## Fixed Evaluator

The fixed evaluator is `run.py`.

The agent must not modify `run.py`, `prepare.py`, the validation split, the metric calculation, or the logging schema.

`run.py` imports `build_model()` from `model.py`, trains the model using the deterministic split created by `prepare.py`, computes validation MAE, and appends the result to `results.tsv`.

The final test set is not used during agent search.

## Evaluation Rule
Every experiment must be evaluated by running:

python3 run.py "<short experiment description>"

The model is trained on the training set and evaluated on the validation set.

Performance is measured using Mean Absolute Error (MAE).

All experiments are compared using validation MAE only.

## Failure Logging Rule

Every experiment must be logged in `results.tsv`, even if it fails.

If an experiment runs successfully, log:
- description
- validation MAE
- runtime seconds
- status = success

If an experiment fails, crashes, or does not return a valid MAE, log:
- description
- val_mae = NA
- runtime seconds
- status = failure
- error message if available

The agent must not manually edit `results.tsv`. Failed runs should be recorded automatically by `run.py`.