from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression


def build_model(preprocessor):
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ])

    return model