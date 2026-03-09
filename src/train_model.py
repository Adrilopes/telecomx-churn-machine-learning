from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def train_logistic_regression(X_train_scaled, y_train):
    """
    Train a Logistic Regression model using scaled training data.
    """
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)
    return model


#def train_random_forest(X_train, y_train):
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def train_random_forest(X_train, y_train):
    """
    Train a Random Forest model using non-scaled training data.
    """
    model = RandomForestClassifier(
        random_state=42,
        n_estimators=300,
        class_weight="balanced"
    )
    
    model.fit(X_train, y_train)
    
    return model