#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download the Behavioral Risk Factor Surveillance System (BRFSS) dataset from Kaggle
into the 'raw' directory.

This script requires the Kaggle API to be installed and configured.

Run this script if you just want to download the dataset. To download and transform the dataset,
run the `prepare_data.py` script instead.
"""

import os

KAGGLE_JSON_FILE = os.path.expanduser("~/.kaggle/kaggle.json")
""" Path to the Kaggle API credentials file. This file is required for downloading datasets from Kaggle. """

DATASET = "cdc/behavioral-risk-factor-surveillance-system"
""" Kaggle dataset identifier for the BRFSS dataset."""

DATA_DIR = os.path.join(".", "data")
""" Directory for all data files, including raw and processed data. """
DATA_ORIG_DIR = os.path.join(DATA_DIR, "orig")
""" Directory for original data files, typically downloaded from Kaggle. """

# === Check if kaggle.json exists ===
if not os.path.exists(KAGGLE_JSON_FILE):
    kaggle_dir = os.path.expanduser("~/.kaggle")
    os.makedirs(kaggle_dir, exist_ok=True)
    print(f"✅ Created directory: '{kaggle_dir}'")

    raise FileNotFoundError(
        f"kaggle.json not found at '{KAGGLE_JSON_FILE}'\n"
        "Get it via: https://www.kaggle.com → Account → Create New API Token.\n"
        f"Place the file at '{KAGGLE_JSON_FILE}'."
    )

# The __init__ of KaggleApi will try to read the kaggle.json file
# and throw an error if it doesn't exist or is not readable.
# The former error is easier to read.
from kaggle.api.kaggle_api_extended import KaggleApi

# === Download dataset ===
api = KaggleApi()
api.authenticate()
api.dataset_download_files(dataset=DATASET, path=DATA_ORIG_DIR, unzip=True)

print(f"✅ Downloaded: '{DATASET}' into '{DATA_ORIG_DIR}'")
