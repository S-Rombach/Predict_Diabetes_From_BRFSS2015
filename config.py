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

MODELS_DIR = os.path.join(BASE_DIR, "models")
""" Directory for machine learning models and related files. """
