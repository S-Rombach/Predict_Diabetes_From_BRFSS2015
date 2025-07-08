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
