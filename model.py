from sklearn.pipeline import Pipeline
from sklearn.ensemble import HistGradientBoostingRegressor


def build_model(preprocessor):
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", HistGradientBoostingRegressor(
            max_iter=200,
            learning_rate=0.05,
            random_state=390))
    ])

    return model