# Week 5 Autonomous Block Log

## Starting Point Before Autonomous Block

**Starting baseline model:** Linear regression  
**Baseline validation MAE:** `0.3825`

**Current best model before Week 5 block:**  
`Random Forest n_estimators = 400 max_features = 0.7`

**Current best validation MAE before Week 5 block:**  
`0.3284`

**Results**
All 6 Week 5 runs were successful but discarded.
Keep = 0
Discard = 6
Crash = 0
Dominant failure type = signal failure

| Run | Description | Validation MAE | Decision |
|---|---|---:|---|
| 1 | Random Forest, `max_depth=20` | 0.3376 | Discard |
| 2 | Random Forest, `max_depth=30` | 0.3326 | Discard |
| 3 | Random Forest, `n_estimators=300`, `max_features=0.7` | 0.3289 | Discard |
| 4 | Extra Trees, `n_estimators=400`, `max_features=0.7` | 0.3340 | Discard |
| 5 | Random Forest, `max_samples=0.8` | 0.3291 | Discard |
| 6 | Gradient Boosting, `n_estimators=200`, `learning_rate=0.05`, `max_depth=3`, `subsample=0.8` | 0.3503 | Discard |
