import numpy as np
import pandas as pd

def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add engineered features for the Sephora rating prediction project.

    This function should only create new predictor columns.
    It should not:
    - change the target variable
    - change the train/validation/test split
    - remove rows
    - access the test set separately
    - change the evaluation metric
    """

    df = df.copy()

    # checks if the product has a sale 

    if "sale_price_usd" in df.columns:
        df["has_sale"] = df["sale_price_usd"].notna().astype(int)

    if "price_usd" in df.columns and "sale_price_usd" in df.columns:
        sale_price = df["sale_price_usd"].fillna(df["price_usd"])

        df["discount_amount"] = df["price_usd"] - sale_price

        df["discount_pct"] = np.where(
            df["price_usd"] > 0,
            df["discount_amount"] / df["price_usd"],
            0
        )

   # checks if product has variety 

    if "child_count" in df.columns:
        df["has_variations"] = (df["child_count"].fillna(0) > 0).astype(int)


   # details on dropped cols 

    if "ingredients" in df.columns:
        ingredients = df["ingredients"].fillna("").astype(str)
        df["has_ingredients"] = (ingredients.str.len() > 0).astype(int)
        df["num_ingredients"] = ingredients.str.count(",") + (ingredients.str.len() > 0).astype(int)

    if "highlights" in df.columns:
        highlights = df["highlights"].fillna("").astype(str)
        df["has_highlights"] = (highlights.str.len() > 0).astype(int)
        df["num_highlights"] = highlights.str.count(",") + (highlights.str.len() > 0).astype(int)

    return df