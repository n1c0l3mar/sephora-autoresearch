import sys
import time
import traceback
import pandas as pd
from pathlib import Path

from sklearn.metrics import mean_absolute_error

from prepare import load_data, build_preprocessor
from model import build_model


RESULTS_FILE = "results.tsv"


def log_result(description, val_mae, runtime_seconds, status, error_message=""):
    results_path = Path(RESULTS_FILE)

    row = {
        "description": description,
        "val_mae": val_mae,
        "runtime_seconds": round(runtime_seconds, 4),
        "status": status,
        "error_message": error_message
    }

    df = pd.DataFrame([row])

    if results_path.exists():
        df.to_csv(results_path, sep="\t", mode="a", header=False, index=False)
    else:
        df.to_csv(results_path, sep="\t", mode="w", header=True, index=False)


def main():
    description = sys.argv[1] if len(sys.argv) > 1 else "no description"

    start_time = time.time()

    try:
        # Load deterministic train/validation data
        (
            X_train,
            X_val,
            X_test,
            y_train,
            y_val,
            y_test,
            numeric_features,
            categorical_features,
        ) = load_data()
        preprocessor = build_preprocessor(numeric_features, categorical_features)

        # Build model from editable model.py
        model = build_model(preprocessor)

        # Train and evaluate
        model.fit(X_train, y_train)
        preds = model.predict(X_val)

        val_mae = mean_absolute_error(y_val, preds)
        runtime_seconds = time.time() - start_time

        # Log successful run
        log_result(
            description=description,
            val_mae=round(val_mae, 4),
            runtime_seconds=runtime_seconds,
            status="success",
            error_message=""
        )

        print(f"Validation MAE: {val_mae:.4f}")
        print(f"Runtime seconds: {runtime_seconds:.4f}")
        print("Status: success")

    except Exception as e:
        runtime_seconds = time.time() - start_time
        error_message = traceback.format_exc().replace("\n", " | ")

        # Log failed run
        log_result(
            description=description,
            val_mae="NA",
            runtime_seconds=runtime_seconds,
            status="failure",
            error_message=error_message
        )

        print("Experiment failed.")
        print(f"Runtime seconds: {runtime_seconds:.4f}")
        print(f"Status: failure")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
