"""
Provides utility functions to evaluate classification models, including scoring, 
confusion matrix reconstruction, and formatting of classification reports.
"""

import pandas as pd
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    balanced_accuracy_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)

from typing import List, Union, Optional, Dict, Any
import numpy as np
from sklearn.base import BaseEstimator
from datetime import datetime

def evaluate_classifier(
    classifier: BaseEstimator,
    labels: List[Union[str, int]],
    target_truth: Union[pd.Series, np.ndarray],
    target_pred: Union[pd.Series, np.ndarray],
    target_pred_proba: Optional[np.ndarray],
    timestamp: datetime,
    model_purpose: str,
    special_features: str,
    avg_mode: str = "weighted",
) -> Dict[str, Any]:
    """
    Evaluates a trained classifier on given predictions and returns a dictionary with performance metrics.

    Parameters
    ----------
    classifier : sklearn.base.BaseEstimator
        Trained classifier object (used for metadata only).
    labels : list
        List of class labels to include in confusion matrix and classification report.
    target_truth : array-like
        True target labels.
    target_pred : array-like
        Predicted target labels.
    target_pred_proba : array-like or None
        Predicted probabilities (used for ROC AUC calculation). Can be None.
    timestamp : datetime
        Timestamp string for unique model identification.
    model_purpose : str
        Description of the model's purpose or context.
    special_features : str
        Indicator string for specific feature configuration used.
    avg_mode : str, default="macro"
        Averaging method for precision, recall, and F1 score.
        Options: {"micro", "macro", "weighted", "samples"}

    Returns
    -------
    dict
        Dictionary containing:
        - model metadata (name, timestamp, class, purpose)
        - evaluation metrics (f1, recall, precision, balanced accuracy, ROC AUC)
        - confusion matrix entries (flattened)
        - classification report (as dict)
    """
    precision_score_val = precision_score(target_truth, target_pred, average=avg_mode)
    recall_score_val = recall_score(target_truth, target_pred, average=avg_mode)
    f1_score_val = f1_score(target_truth, target_pred, average=avg_mode)
    balanced_accuracy_val = balanced_accuracy_score(target_truth, target_pred)

    confusion_matrix_val = confusion_matrix(
        target_truth, target_pred, labels=labels
    )


    roc_auc_score_val = pd.NA
    if target_pred_proba is not None:
        if target_pred_proba.ndim == 2:
            roc_auc_score_val = roc_auc_score(
                target_truth, target_pred_proba, multi_class="ovo", labels=labels
            )
        else:
            roc_auc_score_val = roc_auc_score(
                target_truth==labels[-1], target_pred_proba
            )

    timestamp_str = timestamp.strftime("%Y%m%d%H%M%S")

    model_name = f"{timestamp_str}_{classifier.__class__.__name__}_f1{int(f1_score_val * 1000):05d}_{model_purpose}_{special_features}"

    

    results = {
        "model_name": model_name,
        "timestamp": timestamp_str,
        "model_purpose": model_purpose,
        "model_class": classifier.__class__.__name__,
        "special_features": special_features,
        "predicts": labels,
        "avg_mode": avg_mode,
        "f1": f1_score_val,
        "recall": recall_score_val,
        "precision": precision_score_val,
        "bal_accuracy": balanced_accuracy_val,
        "roc_auc_score": roc_auc_score_val,
        "conf_matrix": {
            f"C_{true_class}_{pred_class}": int(
                confusion_matrix_val[true_class, pred_class]
            )
            for true_class in range(confusion_matrix_val.shape[0])
            for pred_class in range(confusion_matrix_val.shape[1])
        },
        "classification_report": classification_report(
            target_truth, target_pred, digits=3, output_dict=True, labels=labels
        ),
    }

    return results


def get_confusion_matrix_from_results_as_df(results):
    """
    Reconstructs the confusion matrix from the results dictionary as a labeled pandas DataFrame.

    Parameters
    ----------
    results : dict
        Dictionary returned by `evaluate_classifier()` containing:
        - "predicts": list of class labels
        - "conf_matrix": flattened confusion matrix with keys like "C_0_1"

    Returns
    -------
    pandas.DataFrame
        Confusion matrix as a DataFrame with labeled rows (true classes) and columns (predicted classes).
    """
    labels = results["predicts"]
    conf_matrix = results["conf_matrix"]
    rows = {}
    for k, v in conf_matrix.items():
        sp = k.split("_")
        ri = int(sp[1])
        ci = int(sp[2])

        if ri not in rows:
            rows[ri] = {}

        rows[ri][ci] = v

    df = pd.DataFrame([rows[i] for i in sorted(rows.keys())])
    df = df.rename(index={k: v for k, v in enumerate(labels)})
    df = df.rename(columns={k: v for k, v in enumerate(labels)})

    return df

def get_classification_report_from_results_as_df(results, decimals=3):
    """
    Converts the classification report stored in the results dictionary into a formatted DataFrame.

    Parameters
    ----------
    results : dict
        Dictionary returned by `eval_mevaluate_classifierodel()` containing the key "classification_report"
        with the classification report as a nested dict.
    decimals : int, default=3
        Number of decimal places to round the metric values.

    Returns
    -------
    pandas.DataFrame
        Formatted classification report as DataFrame with string values and support as integers.
        The 'accuracy' row includes only the support value for display purposes.
    """
    df = pd.DataFrame(results["classification_report"]).T.round(decimals)

    df["support"] = df["support"].astype(int)

    df = df.astype('str')

    if "accuracy" in df.index:
        df.loc["accuracy", "support"] = df.loc[ "macro avg", "support"]
        df.loc["accuracy", "precision"] = ''
        df.loc["accuracy", "recall"] = ''

    return df