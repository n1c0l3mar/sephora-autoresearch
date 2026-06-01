import pandas as pd
import matplotlib.pyplot as plt


RESULTS_FILE = "results.tsv"
OUTPUT_FILE = "week4_metric_over_time.png"


def main():
    results = pd.read_csv(RESULTS_FILE, sep="\t")
    controlled = results[
        results["description"].str.contains("controlled max_features", na=False)
    ].copy()

    controlled["val_mae"] = pd.to_numeric(controlled["val_mae"], errors="coerce")
    controlled = controlled.dropna(subset=["val_mae"])

    run_numbers = range(1, len(controlled) + 1)

    plt.figure(figsize=(8, 5))
    plt.plot(run_numbers, controlled["val_mae"], marker="o")
    plt.xlabel("Week 4 controlled run")
    plt.ylabel("Validation MAE")
    plt.title("Validation MAE Across Week 4 max_features Runs")
    plt.xticks(list(run_numbers))
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)


if __name__ == "__main__":
    main()
