import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error


TARGET_COL = "rating"
RANDOM_STATE = 390


def load_data(path="product_info.csv"):
    df = pd.read_csv(path)

    drop_cols = [
        "product_id",
        "product_name",
        "brand_id",
        "brand_name",
        "ingredients",
        "highlights",
        "variation_desc",
    ]

    df = df.dropna(subset=[TARGET_COL]).copy()

    X = df.drop(columns=drop_cols + [TARGET_COL], errors="ignore")
    y = df[TARGET_COL]

    numeric_features = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_features = X.select_dtypes(exclude=["number"]).columns.tolist()

    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=0.15, random_state=RANDOM_STATE
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=0.1765, random_state=RANDOM_STATE
    )

    return X_train, X_val, X_test, y_train, y_val, y_test, numeric_features, categorical_features


def build_preprocessor(numeric_features, categorical_features):
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    return preprocessor


def evaluate_model(model, X_val, y_val):
    preds = model.predict(X_val)
    mae = mean_absolute_error(y_val, preds)
    return mae