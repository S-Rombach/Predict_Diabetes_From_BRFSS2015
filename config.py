# config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
""" Base directory of the project, used to construct paths relative to this script. """




DATA_DIR = os.path.join(BASE_DIR, "data")
""" Directory for all data files, including raw and processed data. """
DATA_RAW_DIR = os.path.join(DATA_DIR, "raw")
""" Directory for raw data files, typically the orig after some form of preprocessing. """
DATA_ORIG_DIR = os.path.join(DATA_DIR, "orig")
""" Directory for original data files, typically downloaded from Kaggle. """
DATA_SKRIPTS_DIR = os.path.join(DATA_DIR, "scripts")
""" Directory for scripts related to data processing and transformation. """
DATA_SPLIT_DIR = os.path.join(DATA_DIR, "split")
""" Directory for split data files, such as training, test and validation sets. """

DATA_ORIG_FILENAME = "2015.csv"
""" Name of the original data file downloaded from Kaggle. """
DATA_RAW_FILENAME = "brfss_2015_transformed.csv"
""" Name of the raw data file after transformation. """
TRAIN_RAW_FILENAME = "train_raw_split.csv"
""" Name of the training data file after splitting. """
TEST_RAW_FILENAME = "test_raw_split.csv"
""" Name of the test data file after splitting. """
VALIDATION_RAW_FILENAME = "validation_raw_split.csv"
""" Name of the validation data file after splitting. """


MODELS_DIR = os.path.join(BASE_DIR, "models")
""" Directory for machine learning models and related files. """
