# Journal

This journal intents to capture the thought, reasoning and decision process during the course of this project.

## Baseline results

### Predict two types of diabtes

All shown models are default RandomForests with `class_weight="balanced"`. Models are referenced by their timestamp for brevity.

The majority class of healthy people prevents effective learning of patterns of diabetes. The baseline model `20250701140915` heavily favors class `no dia` and only predicts class `dia` once.

_Confusion Matrix of 20250701140915_

| T \ P  |   no dia |   pre |   dia |
|--------|----------|-------|-------|
| no dia |    36761 |   958 |    65 |
| pre    |     4766 |   934 |    16 |
| dia    |      723 |    62 |     1 |

Neither default SMOTE (model `20250701155146`) nor sole upsampling of class `pre` (model `20250701161944`) improves the prediction.

_Confusion Matrix of 20250701161944_

| T \ P  |   no dia |   pre |   dia |
|--------|----------|-------|-------|
| no dia |    35278 |  2402 |   104 |
| pre    |     3906 |  1783 |    27 |
| dia    |      632 |   152 |     2 |

A baseline model (model `20250702162131`) with smote to distinguish classes `pre` and `dia` confirms that the data lacks sufficient structure to distinguish class `pre` from class `dia`.

_Confusion Matrix of 20250702162131_

| T \ P  |  pre | no dia |
|--------|------|--------|
| pre    | 5631 |     85 |
| no dia |  771 |     15 |

A baseline model (model `20250702154506`) with smote to distinguish classes `no dia` vs merged `pre` and `dia` improves the f1 (0.8297) sligthly, but balanced accuracy (0.6267) and auc (0.8025) strongly. See table _Metrics of discussed models_ below.

_Confusion Matrix of 20250702154506_

| T \ P  |   no dia |   dia |
|--------|----------|-------|
| no dia |    35085 |  2699 |
| dia    |     4389 |  2113 |

_Metrics of discussed models_

|          model | model_purpose   | predicts         | features   |       f1 |   recall |   precision |   bal_accuracy |   roc_auc_score |
|----------------|-----------------|------------------|------------|----------|----------|-------------|----------------|-----------------|
| 20250702154506 | baseline        | no dia, dia      | smote      | 0.829746 | 0.839949 |    0.822788 |       0.626772 |        0.802578 |
| 20250701155146 | baseline        | no dia, pre, dia | smote      | 0.821597 | 0.836901 |    0.80927  |       0.416051 |        0.682203 |
| 20250702162131 | baseline        | pre, dia         | smote      | 0.821108 | 0.868348 |    0.791374 |       0.502107 |        0.603116 |
| 20250701140915 | baseline        | no dia, pre, dia |            | 0.815238 | 0.851195 |    0.80425  |       0.379199 |        0.687022 |

#### Conclusion

Differentiation between `no dia`, `pre` and `dia` does not seem promising. Differentiation between `pre` and `dia` works better than differentiation between all three, but differentiiation between `no dia` and some form of diabetes even better. A hierarchical approach to first assess the presence of diabetes and the exact form afterwards seems more promising.

The aim of this project is therefore revised to **predict any form of diabetes**.

### Predict presence of any form of diabetes

Overall precision, the recall of `dia`, balanced accuracy and roc-auc score improve when predicting just two classes (see `20250702154506`) with Random Forests. Optimizing hyperparameters (see `20250703130629`) further lead to improved performance.

## Other estimators

Other estimators were used to train a `no dia` vs `dia` baseline model and a model with optimized hyperparameters. The following table shows the results of the optimized models, sorted by descending f1:

|           model | model_class                    | predicts    |       f1 |   recall |   precision |   bal_accuracy |   roc_auc_score |
|-----------------|--------------------------------|-------------|----------|----------|-------------|----------------|-----------------|
|  20250710164643 | HistGradientBoostingClassifier | dia, no dia | 0.833594 | 0.837443 |    0.830264 |       0.653444 |        0.813395 |
|  20250709203156 | GradientBoostingClassifier     | dia, no dia | 0.820847 | 0.804498 |    0.847974 |       0.724861 |        0.825389 |
|  20250709202835 | ExtraTreesClassifier           | dia, no dia | 0.819279 | 0.815224 |    0.823828 |       0.654747 |        0.783459 |
|  20250709203410 | BaggingClassifier              | dia, no dia | 0.808833 | 0.800569 |    0.818941 |       0.649533 |        0.757922 |
|  20250709205009 | MLPClassifier                  | dia, no dia | 0.789046 | 0.76006  |    0.848902 |       0.732371 |        0.812609 |
|  20250709203308 | AdaBoostClassifier             | dia, no dia | 0.787554 | 0.757756 |    0.85043  |       0.73586  |        0.815025 |
|  20250709202238 | DecisionTreeClassifier         | dia, no dia | 0.783254 | 0.770153 |    0.799699 |       0.610762 |        0.611623 |
|  20250709234440 | LogisticRegression             | dia, no dia | 0.770364 | 0.734724 |    0.853811 |       0.741589 |        0.815147 |
|  20250710000602 | RidgeClassifier                | dia, no dia | 0.765508 | 0.728289 |    0.855673 |       0.744693 |                 |
|  20250709203414 | KNeighborsClassifier           | dia, no dia | 0.76431  | 0.732263 |    0.823485 |       0.672979 |        0.731368 |
|  20250709223829 | GaussianNB                     | dia, no dia | 0.693087 | 0.640677 |    0.851653 |       0.716205 |        0.770498 |

## Feature Engineering

Numerical columns `BMI`, `MentHlth`, `PhysHlth` were divided into categories by different thresholds. A random-forest and a logistic-regression model were trained and optimized along different thresholds and hyperparameters.

Differences between their baseline and optimized versions are small (~.05 f1-score). This is probably due to the fact the BMI is the most important feature and categorization does not add information. The following table shows the results of the optimized models, sorted by model class and descending f1:

|   timestamp_str | model_class            | predicts    |       f1 |   recall |   precision |   bal_accuracy |   roc_auc_score |  class die recall |
|-----------------|------------------------|-------------|----------|----------|-------------|----------------|-----------------|-------------------|
|  20250722210637 | LogisticRegression     | dia, no dia | 0.815105 | 0.81335  |    0.816942 |       0.63716  |        0.773281 |          0.387727 |
|  20250709234440 | LogisticRegression     | dia, no dia | 0.770364 | 0.734724 |    0.853811 |       0.741589 |        0.815147 |          0.751307 |
|  20250709202244 | LogisticRegression     | dia, no dia | 0.769785 | 0.733821 |    0.855063 |       0.744179 |        0.819652 |          0.758843 |
|  20250702154506 | RandomForestClassifier | dia, no dia | 0.829746 | 0.839949 |    0.822788 |       0.626772 |        0.802578 |          0.324977 |
|  20250709202524 | RandomForestClassifier | dia, no dia | 0.826173 | 0.823488 |    0.829097 |       0.663665 |        0.802101 |          0.437404 |
|  20250711123224 | RandomForestClassifier | dia, no dia | 0.826173 | 0.823488 |    0.829097 |       0.663665 |        0.802101 |          0.437404 |
|  20250703130629 | RandomForestClassifier | dia, no dia | 0.785673 | 0.753918 |    0.85815  |       0.753155 |        0.813622 |          0.752076 |

Indeed, optimization efforts focused on hyperparameter tuning and feature selection did not yield significant improvements in model performance, but rather diminished the recall of the `dia` class severly (from ~0.75 to ~0.38 for Logistic Regression and ~0.43 for Random Forest). The best models remain the ones trained on the original features without additional feature engineering.
