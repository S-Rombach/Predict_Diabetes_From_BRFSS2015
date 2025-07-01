#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transform the Behavioral Risk Factor Surveillance System (BRFSS) dataset
into a format suitable for analysis.
This script processes the raw data files downloaded from Kaggle and saves
the transformed data into the 'data' directory.

============================================================================
DISCLAIMER: This script (and this alone) is a modification of Alex Teboul's
original Diabetes Health Indicators Dataset Notebook. The idea, some decisions
and names are inspired by his work.

The original notebook is available at:
https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system
============================================================================

I wanted to keep the data as close to the original dataset as possible, i.e.,
keeping missing values while also introducing readable values.
"""

import os
import pandas as pd
from pathlib import Path
import sys
from sklearn.model_selection import train_test_split

# Ensure the script can find the config.py file in the project root
sys.path.insert(
    0,
    next(
        (
            str(p)
            for p in [Path.cwd(), *Path.cwd().parents]
            if (p / "config.py").exists()
        ),
        "",
    ),
)

from config import (
    DATA_RAW_DIR,
    DATA_SPLIT_DIR,
    DATA_RAW_FILENAME,
    TRAIN_RAW_FILENAME,
    TEST_RAW_FILENAME,
    VALIDATION_RAW_FILENAME,
)

os.makedirs(DATA_SPLIT_DIR, exist_ok=True)

df_raw = pd.read_csv(os.path.join(DATA_RAW_DIR, DATA_RAW_FILENAME))

X_train, X_temp = train_test_split(df_raw, random_state=42, test_size=0.15)
X_val, X_test = train_test_split(X_temp, random_state=42, test_size=0.33)


X_train.to_csv(os.path.join(DATA_SPLIT_DIR, TRAIN_RAW_FILENAME), index=False)
X_val.to_csv(os.path.join(DATA_SPLIT_DIR, VALIDATION_RAW_FILENAME), index=False)
X_test.to_csv(os.path.join(DATA_SPLIT_DIR, TEST_RAW_FILENAME), index=False)
