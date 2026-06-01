import pandas as pd
import matplotlib.pyplot as plt

results = pd.read_csv("results.tsv", sep="\t")

week5 = results[results["description"].str.startswith("week5", na=False)].copy()

week5["val_mae"] = pd.to_numeric(week5["val_mae"], errors="coerce")
week5 = week5.dropna(subset=["val_mae"]).reset_index(drop=True)

week5["run_order"] = range(1, len(week5) + 1)
feature_engineering_run = week5[
    week5["description"].eq("week5 feature eng add brand_name categorical")
]["run_order"]

plt.figure(figsize=(8, 5))
plt.plot(week5["run_order"], week5["val_mae"], marker="o")

if not feature_engineering_run.empty:
    feature_x = feature_engineering_run.iloc[0]
    plt.axvline(
        feature_x,
        color="tab:green",
        linestyle="--",
        linewidth=1,
        alpha=0.7,
        label="Feature engineering added"
    )
    plt.legend()

plt.xlabel("Week 5 autonomous run")
plt.ylabel("Validation MAE")
plt.title("Week 5 Validation MAE: Model Tuning Before and After Feature Engineering")
plt.xticks(week5["run_order"])
plt.grid(True, alpha=0.3)


for i, row in week5.iterrows():
    plt.annotate(
        f"{row['val_mae']:.4f}",
        (row["run_order"], row["val_mae"]),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
        fontsize=8
    )

plt.tight_layout()
plt.savefig("week5_metric_trajectory.png", dpi=200)
plt.close()
