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

## Week 5 Autonomous Block Rules

The agent should run a longer autonomous experiment block while preserving a complete research log.

The agent may only modify:
- `model.py`

The agent must not modify:
- `run.py`
- `prepare.py`
- `product_info.csv`
- `results.tsv` manually
- `README.md`
- `program.md`

The only way `results.tsv` should change is by running:

```bash
python3 run.py "<experiment description>"
```

Each run in the autonomous block must include:
- a clear experiment description
- the model change attempted
- validation MAE or `NA`
- runtime seconds
- status: `success` or `failure`
- decision: `keep`, `discard`, or `crash`
- error message if applicable

Rollback rule:
- If a run is `keep`, leave `model.py` as the new best version.
- If a run is `discard` or `crash`, restore `model.py` to the current best valid working version before continuing.

The agent should preserve a complete trace of:
- what it tried
- what changed
- what was kept
- what was discarded
- what crashed
- what was rolled back
- which changes appear meaningful

The numeric outcome should be recorded in `results.tsv`; the explanation of the model change and rollback decision should be recorded in the agent's summary. 

## Week 5 Feature-Engineered Model Block Rules

The project now includes a fixed feature-engineering setup.

For this block, the engineered feature set is treated as frozen. The agent should not create new engineered features, remove engineered features, or change the feature-engineering logic.

The goal of this block is to test whether model and hyperparameter changes can improve validation MAE using the updated feature set.

For this block, the agent may only modify:
- `model.py`

The agent must not modify:
- `feature_engineering.py`
- `prepare.py`
- `run.py`
- `product_info.csv`
- `results.tsv` manually
- `README.md`
- `program.md`

The agent must keep:
- the current feature-engineering logic fixed
- `brand_name` included as a categorical feature
- the target variable fixed as `rating`
- the validation metric fixed as MAE
- the deterministic train/validation/test split unchanged
- `random_state = 390`
- the final test set unused during search

Each experiment must be evaluated by running:

```bash
python3 run.py "<experiment description>"
```