
# Project

## Description

This project aims to predict diabetes in patients using various machine learning models. The dataset used for this project is the Behavioral Risk Factor Surveillance System (BRFSS) 2015 dataset, which contains information on health-related risk behaviors, chronic health conditions, and use of preventive services. The project includes exploratory data analysis, model training, hyperparameter optimization, and evaluation of different classifiers such as Random Forest, Logistic Regression, and Neural Networks. The models are trained to predict two types of diabetes and the presence of diabetes in individuals based on their health history. The project also explores the use of SMOTE (Synthetic Minority Over-sampling Technique) for handling class imbalance in the dataset. The results are evaluated using F1-score and class recall.

## Inspiration

This project was inspired by the work ([the adapted dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)) of Alex Teboul on the [BRFSS 2015 dataset](https://www.kaggle.com/competitions/predict-diabetes-from-brfss2015), which is available on Kaggle. He in turn was inspired by the [CDC paper](https://www.cdc.gov/pcd/issues/2019/19_0109.htm) that discusses the prevalence of diabetes and its risk factors.

## Setup

### Prerequisites

#### package manager uv installed

Look [here](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) for installation instructions.

#### Python 3.10 or higher

You need Python 3.10 or higher installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

#### kaggle account

You need a Kaggle account to download the dataset. Create an account on [Kaggle](https://www.kaggle.com/) if you don't have one.

### Prepare data

Execute the following in the project folder:

``` powershell
uv sync
& ./.venv/Scripts/python.exe ./data/scripts/download_data.py
& ./.venv/Scripts/python.exe ./data/scripts/transform_data.py
& ./.venv/Scripts/python.exe ./data/scripts/split_data.py
```

At this point all notebooks and code are fully functional.

## Aim

### Metric

The primary metrics are the f1-score and class recall.

### Primary: Predict two types of diabetes

This project aims to predict two types of diabetes in a person or if the person is healthy (i.e. has no diabetes) based on the history of the patient.

### Secondary: Predict the presence of diabetes

This project aims to predict whether a person has any form of diabetes captured in the dataset.

## Results

All evaluation was done on held-out validation and test set.

## Data

* Data source: <https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system>
* Related paper: <https://www.cdc.gov/pcd/issues/2019/19_0109.htm>

## What I used intensively

* Random Forest
* Logistic Regression
* SMOTE
* Random Oversampling
* Bayesian Optimization

## File Structure

* eda/eda_three_classes.ipynb: Exploratory data analysis of the training set.
* model_training/
  * dt_base_line_model.ipynb: Baseline model using Decision Trees.
  * lgreg_base_line_model_smote.ipynb: Training of a Logistic Regression model with upsampling by SMOTE.
  * multclf_base_line_model_smote.ipynb: Training of different classifiers as baselines with upsampling by SMOTE.
  * multclf_hyperparam_opt_bayesian.ipynb: Hyperparameter optimization for multiple classifiers using Bayesian optimization.
  * nn_base_line_model.ipynb: Baseline model using Neural Networks.
  * rf_base_line_model.ipynb: Baseline model using Random Forest.
  * rf_base_line_model_smote.ipynb: Training of a Random Forest model with upsampling by SMOTE.
  * rf_hyperparam_opt_bayesian.ipynb: Hyperparameter optimization for Random Forest using Bayesian optimization.
  * rf_hyperparam_opt_bayesian_feateng.ipynb: Hyperparameter optimization for Random Forest using Bayesian optimization with feature engineering.

* src/
  * config.py: Configuration file containing paths and constants.
  * model_evaluation.py: Contains functions for evaluating models.
  * transformers.py: Contains custom transformers for preprocessing data.
