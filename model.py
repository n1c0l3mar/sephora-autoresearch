from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor


def build_model(preprocessor):
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=1000,
            min_samples_leaf=1,
            max_features=0.7,
            random_state=390,
            n_jobs=-1))
    ])

    return model
