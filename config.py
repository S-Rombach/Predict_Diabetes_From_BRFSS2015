# config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
""" Base directory of the project, used to construct paths relative to this script. """

DATA_DIR = os.path.join(BASE_DIR, "data")
""" Directory for all data files, including raw and processed data. """
RAWDATA_DIR = os.path.join(DATA_DIR, "raw")
""" Directory for raw data files, typically the orig after some form of preprocessing. """
MODELS_DIR = os.path.join(BASE_DIR, "models")
""" Directory for machine learning models and related files. """
ORIGDATA_DIR = os.path.join(DATA_DIR, "orig")
""" Directory for original data files, typically downloaded from Kaggle. """


KAGGLE_JSON_FILE = os.path.expanduser("~/.kaggle/kaggle.json")
""" Path to the Kaggle API credentials file. This file is required for downloading datasets from Kaggle. """