
# Project

![Python](https://img.shields.io/badge/python-3.12%2B-blue)


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

## Run

After completing the setup, you can run any number of the notebooks in the `model_training` folder to train and evaluate the models. The model and its results will be saved in the `models` folder. 

If you want to classify the presence of some diabetes vs no diabetes, you may have to merge the `pre` and `dia` classes into one class `dia`. This can be done by replacing the `pre` class with `dia` in the training and validation datasets. In the _Load and transform train and validation data_ section of the notebooks, you can modify the code to merge the classes as follows:

Replace the following code snippet in the notebook:

``` python
target_train_raw = df_train_raw["Diabetes_012"]
...
target_val_raw = df_val_raw["Diabetes_012"]
```

with:

``` python
target_train_raw = df_train_raw["Diabetes_012"].replace({"pre": "dia"})
...
target_val_raw = df_val_raw["Diabetes_012"].replace({"pre": "dia"})
```

## Aim

### Metric

The primary metrics are the f1-score and class recall.

### Primary: Predict two types of diabetes

This project aims to predict two types of diabetes in a person or if the person is healthy (i.e. has no diabetes) based on the history of the patient.

### Secondary: Predict the presence of diabetes

This project aims to predict whether a person has any form of diabetes captured in the dataset.

## Results

The project successfully predicts the presence of diabetes (merged classes `pre` and `dia`) using a Logistic Regression model on feature-engineered data.  

| Metric            | Score   |
|-------------------|--------:|
| F1-score          | 0.770   |
| Recall (class `dia`) | 0.772   |
| Balanced Accuracy | 0.750   |
| ROC-AUC           | 0.824   |

All evaluation was conducted on held-out validation and test sets.

For more details on the results, see the [Journal.md](Journal.md) file.

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

* Journal.md: Journal of the project, capturing the thought, reasoning and decision process during the course of this project.
* eda/eda_three_classes.ipynb: Exploratory data analysis of the training set.
* model_training/
  * best_model_logreg.ipynb: Best overall model using Logistic Regression.
  * dt_base_line_model.ipynb: Baseline model using Decision Trees.
  * lgreg_base_line_model_smote.ipynb: Training of a Logistic Regression model with upsampling by SMOTE.
  * multclf_base_line_model_smote.ipynb: Training of different classifiers as baselines with upsampling by SMOTE.
  * multclf_hyperparam_opt_bayesian.ipynb: Hyperparameter optimization for multiple classifiers using Bayesian optimization.
  * nn_base_line_model.ipynb: Baseline model using Neural Networks.
  * rf_base_line_model.ipynb: Baseline model using Random Forest.
  * rf_base_line_model_smote.ipynb: Training of a Random Forest model with upsampling by SMOTE.
  * rf_hyperparam_opt_bayesian.ipynb: Hyperparameter optimization for Random Forest using Bayesian optimization.
  * rf_hyperparam_opt_bayesian_feateng.ipynb: Hyperparameter optimization for Random Forest using Bayesian optimization with feature engineering.
* models/
  * compare_models.ipynb: Notebook to compare different models and their performance. After at least one model has been trained, this notebook can be run to compare the models.
  * create_feature_importance.ipynb: Notebook to create feature importance plots for the models.
  * model_folder/
    Each model is saved in a separate folder with its name. The models name consist of a timestamp, the classifier name, the achieved f1-score and its purpose (free text). It contains the following files, which all start with the model's name (same as the folder name):
    * *.model_params.json: JSON files containing the parameters of the trained classifier.
    * *.model.pkl: Pickle files containing the trained classifier.
    * *.model.txt: Files containing the model's text representation for easier access.
    * *.pipeline.pkl: Pickle files containing the trained pipeline, which includes preprocessing steps but not the classifier.
    * *.pipeline_params.txt: Files containing the pipeline's text representation for easier access.
    * *.model_results.json: JSON files containing the results of the model evaluation.

* src/
  * config.py: Configuration file containing paths and constants.
  * model_evaluation.py: Contains functions for evaluating models.
  * transformers.py: Contains custom transformers for preprocessing data.
* data/scripts/
  See `Prepare data` section above for details on how to call these scripts.
  * download_data.py: Script to download the dataset from Kaggle.
  * transform_data.py: Script to transform the raw data into a usable format.
  * split_data.py: Script to split the data into training, validation, and test sets.
