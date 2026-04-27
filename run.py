import sys
import time
import csv
import os

from prepare import load_data, build_preprocessor, evaluate_model
from model import build_model


RESULTS_FILE = "results.tsv"


def main():
    description = sys.argv[1] if len(sys.argv) > 1 else "no description"

    X_train, X_val, X_test, y_train, y_val, y_test, numeric_features, categorical_features = load_data()

    preprocessor = build_preprocessor(numeric_features, categorical_features)
    model = build_model(preprocessor)

    start = time.time()
    model.fit(X_train, y_train)
    runtime = time.time() - start

    val_mae = evaluate_model(model, X_val, y_val)

    file_exists = os.path.exists(RESULTS_FILE)

    with open(RESULTS_FILE, "a", newline="") as f:
        writer = csv.writer(f, delimiter="\t")

        if not file_exists:
            writer.writerow(["description", "val_mae", "runtime_seconds", "status"])

        writer.writerow([description, round(val_mae, 4), round(runtime, 4), "logged"])

    print(f"Description: {description}")
    print(f"Validation MAE: {val_mae:.4f}")
    print(f"Runtime seconds: {runtime:.4f}")
    print(f"Result logged to {RESULTS_FILE}")


if __name__ == "__main__":
    main()