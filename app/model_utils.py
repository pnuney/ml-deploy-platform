from typing import Any, List


#For now this is a fake model so you can get the platform running
#Later you can swap this out to load from S3 or a local file


class DummyModel:
    def predict_proba(self, X: list[list[float]]) -> list[list[float]]:
        # Just use a simple function of the first feature
        probs = []
        for row in X:
            x0 = row[0] if row else 0.0
            p1 = 1 / (1 + pow(2.71828, -x0))
            p0 = 1 - p1
            probs.append([p0, p1])
        return probs


def load_model() -> Any:
    #Later: load from joblib file or S3
    #For now: return dummy model
    return DummyModel()


def predict_proba(model: Any, features: List[float]) -> float:
    proba = model.predict_proba([features])[0][1]
    return float(proba)
