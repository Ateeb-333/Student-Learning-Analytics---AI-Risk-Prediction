import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score, precision_score, recall_score, \
    f1_score


class PerformancePredictor:
    def __init__(self):
        self.model = RandomForestRegressor(random_state=42)

    def train(self, features: pd.DataFrame):
        if "score" not in features.columns:
            # Auto-generate synthetic score if missing
            features = features.copy()
            features["score"] = (
                                        features["accuracy_rate"] * 100 +
                                        features["practice_test_score"] * 100
                                ) / 2

        X = features.drop(columns=["score"])
        y = features["score"]
        self.model.fit(X, y)

    def evaluate(self, features: pd.DataFrame):
        if "score" not in features.columns:
            return {"MAE": 0, "MSE": 0, "RMSE": 0}

        X = features.drop(columns=["score"])
        y = features["score"]
        predictions = self.model.predict(X)

        return {
            "MAE": mean_absolute_error(y, predictions),
            "MSE": mean_squared_error(y, predictions),
            "RMSE": mean_squared_error(y, predictions) ** 0.5
        }

    def predict(self, features: pd.DataFrame):
        return self.model.predict(features.drop(columns=["score"], errors="ignore"))


class RiskClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(random_state=42)

    def train(self, features: pd.DataFrame):
        if "score" not in features.columns:
            features = features.copy()
            features["score"] = (
                                        features["accuracy_rate"] * 100 +
                                        features["practice_test_score"] * 100
                                ) / 2

        # Define "at-risk" = score below 60
        y = (features["score"] < 60).astype(int)
        X = features.drop(columns=["score"])
        self.model.fit(X, y)

    def evaluate(self, features: pd.DataFrame):
        if "score" not in features.columns:
            return {"Accuracy": 0, "Precision": 0, "Recall": 0, "F1": 0}

        y = (features["score"] < 60).astype(int)
        X = features.drop(columns=["score"])
        predictions = self.model.predict(X)

        return {
            "Accuracy": accuracy_score(y, predictions),
            "Precision": precision_score(y, predictions),
            "Recall": recall_score(y, predictions),
            "F1": f1_score(y, predictions)
        }

    def predict(self, features: pd.DataFrame):
        return self.model.predict(features.drop(columns=["score"], errors="ignore"))
