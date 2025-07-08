
# Project

## Description

## Setup

### Conditions

* uv installed
* kaggle account

### Prepare data

In the project folder:

```
uv init
& ./.venv/Scripts/python.exe ./data/scripts/download_data.py
& ./.venv/Scripts/python.exe ./data/scripts/transform_data.py
& ./.venv/Scripts/python.exe ./data/scripts/split_data.py
```

## Aim

### Metric

The primary metric is f1-score.,

### Primary: Predict two types of diabtes

This project aims to predict two types of diabtes in a person or if the person is healthy (i.e. has no diabetes) based on the history of the patient.

### Secondary: Predict the presence of diabtes

This project aims to predict whether a person has diabetes.

## File Structure

TODO

## Results

All evaluation was done on a held-out test set.

### Machine specifications

| | |
| - | - |
| number of physical cores | 4 |
| core frequency | 1.8 GHz |
| RAM | 17 GB |

## Data

Data source: <https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system>
Related paper: <https://www.cdc.gov/pcd/issues/2019/19_0109.htm>
TODO

## What I used

RF

## What I learned

categories are hard to use for feature engineering

## What I do different next time

No timestamp names for models