"""Plotting helpers for evaluation."""
import matplotlib.pyplot as plt
import seaborn as sns


def plot_confusion_matrix(cm, labels=(0, 1, 2, 3), title="Confusion Matrix"):
    """Plot a confusion matrix heatmap."""
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=labels, yticklabels=labels, ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(title)
    plt.tight_layout()
    return fig


def plot_feature_importance(model, feature_names, top_n=10):
    """Plot top-N feature importances (works for tree-based models)."""
    if not hasattr(model, "feature_importances_"):
        raise ValueError("Model has no feature_importances_ attribute.")
    importances = sorted(
        zip(feature_names, model.feature_importances_),
        key=lambda x: x[1], reverse=True
    )[:top_n]
    names, values = zip(*importances)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=list(values), y=list(names), ax=ax)
    ax.set_title(f"Top {top_n} Feature Importances")
    ax.set_xlabel("Importance")
    plt.tight_layout()
    return fig
