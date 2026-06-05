"""Feature scaling and preprocessing."""
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def scale_features(X_train, X_test):
    """Standardize features (fit on train, transform both)."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler


def make_train_test_split(X, y, test_size=0.2, random_state=42):
    """Stratified train/test split."""
    return train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )
