from pathlib import Path

from sklearn.metrics import mean_absolute_error

from model import build_model
from prepare import build_preprocessor, load_data


RESULT_PATH = Path("final_deliverables/final_test_result.md")


def main():
    if RESULT_PATH.exists():
        raise RuntimeError(
            f"{RESULT_PATH} already exists. The one-time final test evaluation "
            "has already been recorded."
        )

    (
        X_train,
        _X_val,
        X_test,
        y_train,
        _y_val,
        y_test,
        numeric_features,
        categorical_features,
    ) = load_data()

    preprocessor = build_preprocessor(numeric_features, categorical_features)
    model = build_model(preprocessor)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    test_mae = mean_absolute_error(y_test, predictions)

    result = (
        "# Final Test Result\n\n"
        "This file records the one-time final evaluation of the locked best "
        "model on the held-out test set. The final test set was not used "
        "during model tuning, and no tuning should occur after this result.\n\n"
        "## Locked Model\n\n"
        "- `RandomForestRegressor`\n"
        "- `n_estimators=400`\n"
        "- `max_features=0.7`\n"
        "- `random_state=390`\n"
        "- `n_jobs=-1`\n\n"
        "## One-Time Held-Out Test Evaluation\n\n"
        f"**Final test MAE:** `{test_mae:.4f}`\n"
    )

    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with RESULT_PATH.open("x", encoding="utf-8") as result_file:
        result_file.write(result)

    print(f"Final test MAE: {test_mae:.4f}")
    print(f"Recorded one-time result in {RESULT_PATH}")


if __name__ == "__main__":
    main()
