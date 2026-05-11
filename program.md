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

## Week 5 Feature Engineering Extension Rules

After the Week 5 model-only autonomous block failed to improve the current best validation MAE, the agent may run a controlled feature-engineering extension.

This extension is not a restart of the project. The evaluator, metric, deterministic split, target variable, and logging rules remain fixed.

For this feature-engineering extension only, the agent may modify:
- `feature_engineering.py`
- `prepare.py`
- `model.py`

The agent may modify `prepare.py` ONLY to:
- import `add_engineered_features()` from `feature_engineering.py`
- apply engineered features after loading `product_info.csv`
- apply engineered features before dropping columns and before the deterministic train/validation/test split
- update feature lists or dropped columns only as needed to include engineered predictors

The agent must not modify:
- `run.py`
- `product_info.csv`
- `results.tsv` manually
- the target variable
- the validation metric
- the train/validation/test split proportions
- `random_state = 390`
- the final test set plan

Each feature-engineering experiment must be evaluated by running:

```bash
python3 run.py "<experiment description>"
```