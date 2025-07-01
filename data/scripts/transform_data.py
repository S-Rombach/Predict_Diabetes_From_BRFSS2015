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

from config import DATA_RAW_DIR, DATA_ORIG_DIR, DATA_ORIG_FILENAME, DATA_RAW_FILENAME

# Ensure the raw data directory exists
os.makedirs(DATA_RAW_DIR, exist_ok=True)

new_column_names = {
    "DIABETE3": "Diabetes_012",
    "_RFHYPE5": "HighBP",
    "TOLDHI2": "HighChol",
    "_CHOLCHK": "CholCheck",
    "_BMI5": "BMI",
    "SMOKE100": "Smoker",
    "CVDSTRK3": "Stroke",
    "_MICHD": "HeartDiseaseorAttack",
    "_TOTINDA": "PhysActivity",
    "_FRTLT1": "Fruits",
    "_VEGLT1": "Veggies",
    "_RFDRHV5": "HvyAlcoholConsump",
    "HLTHPLN1": "AnyHealthcare",
    "MEDCOST": "NoDocbcCost",
    "GENHLTH": "GenHlth",
    "MENTHLTH": "MentHlth",
    "PHYSHLTH": "PhysHlth",
    "DIFFWALK": "DiffWalk",
    "SEX": "Sex",
    "_AGEG5YR": "Age",
    "EDUCA": "Education",
    "INCOME2": "Income",
}


df = pd.read_csv(
    os.path.join(DATA_ORIG_DIR, DATA_ORIG_FILENAME),
    usecols=list(new_column_names.keys()),
)

# Sort columns
df = df[list(new_column_names.keys())]

df = df.dropna(how="all")

# DIABETE3
# going to make this ordinal. 0 is for no diabetes or only during pregnancy
# 1 is for pre-diabetes or borderline diabetes, 2 is for yes diabetes
# Remove all 7 (dont knows)
# Remove all 9 (refused)
df["DIABETE3"] = df["DIABETE3"].replace({2: "no dia", 3: "no dia", 1: "pre", 4: "dia"})
df = df[df.DIABETE3.notna()]
df = df[df.DIABETE3 != 7]
df = df[df.DIABETE3 != 9]

# 1 _RFHYPE5
# Change 1 to 0 so it represetnts No high blood pressure and
# 2 to 1 so it represents high blood pressure
df["_RFHYPE5"] = df["_RFHYPE5"].replace({1: "n", 2: "y", 9: pd.NA})

# 2 TOLDHI2
# Change 2 to 0 because it is No
# Remove all 7 (dont knows)
# Remove all 9 (refused)
df["TOLDHI2"] = df["TOLDHI2"].replace({1: "y", 2: "n", 7: pd.NA, 9: pd.NA})

# 3 _CHOLCHK
# Change 3 to 0 and 2 to 0 for Not checked cholesterol in past 5 years
# Remove 9
df["_CHOLCHK"] = df["_CHOLCHK"].replace({1: "y", 3: "n", 2: "n", 9: pd.NA})

# 4 _BMI5 (no changes, just note that these are BMI * 100.
# So for example a BMI of 4018 is really 40.18)
df["_BMI5"] = df["_BMI5"].div(100).round(2)

# 5 SMOKE100
# Change 2 to 0 because it is No
# Remove all 7 (dont knows)
# Remove all 9 (refused)
df["SMOKE100"] = df["SMOKE100"].replace({1: "y", 2: "n", 7: pd.NA, 9: pd.NA})

# 6 CVDSTRK3
# Change 2 to 0 because it is No
# Remove all 7 (dont knows)
# Remove all 9 (refused)
df["CVDSTRK3"] = df["CVDSTRK3"].replace({1: "y", 2: "n", 7: pd.NA, 9: pd.NA})

# 7 _MICHD
# Change 2 to 0 because this means did not have MI or CHD
df["_MICHD"] = df["_MICHD"].replace({1: "y", 2: "n"})

# 8 _TOTINDA
# 1 for physical activity
# change 2 to 0 for no physical activity
# Remove all 9 (don't know/refused)
df["_TOTINDA"] = df["_TOTINDA"].replace({1: "y", 2: "n", 9: pd.NA})

# 9 _FRTLT1
# Change 2 to 0. this means no fruit consumed per day.
# 1 will mean consumed 1 or more pieces of fruit per day
# remove all dont knows and missing 9
df["_FRTLT1"] = df["_FRTLT1"].replace({1: "y", 2: "n", 9: pd.NA})

# 10 _VEGLT1
# Change 2 to 0. this means no vegetables consumed per day.
# 1 will mean consumed 1 or more pieces of vegetable per day
# remove all dont knows and missing 9
df["_VEGLT1"] = df["_VEGLT1"].replace({1: "y", 2: "n", 9: pd.NA})

# 11 _RFDRHV5
# Change 1 to 0 (1 was no for heavy drinking).
# Change all 2 to 1 (2 was yes for heavy drinking)
# remove all dont knows and missing 9
df["_RFDRHV5"] = df["_RFDRHV5"].replace({1: "n", 2: "y", 9: pd.NA})

# 12 HLTHPLN1
# 1 is yes, change 2 to 0 because it is No health care access
# remove 7 and 9 for don't know or refused
df["HLTHPLN1"] = df["HLTHPLN1"].replace({1: "y", 2: "n", 7: pd.NA, 9: pd.NA})

# 13 MEDCOST
# Change 2 to 0 for no, 1 is already yes
# remove 7 for don/t know and 9 for refused
df["MEDCOST"] = df["MEDCOST"].replace({1: "y", 2: "n", 7: pd.NA, 9: pd.NA})

# 14 GENHLTH
# This is an ordinal variable that I want to keep (1 is Excellent -> 5 is Poor)
# Remove 7 and 9 for don't know and refused
df["GENHLTH"] = df["GENHLTH"].replace(
    {
        1: "excellent",
        2: "very good",
        3: "good",
        4: "fair",
        5: "poor",
        7: pd.NA,
        9: pd.NA,
    }
)

# 15 MENTHLTH
# already in days so keep that, scale will be 0-30
# change 88 to 0 because it means none (no bad mental health days)
# remove 77 and 99 for don't know not sure and refused
df["MENTHLTH"] = df["MENTHLTH"].replace({88: 0, 77: pd.NA, 99: pd.NA})

# 16 PHYSHLTH
# already in days so keep that, scale will be 0-30
# change 88 to 0 because it means none (no bad mental health days)
# remove 77 and 99 for don't know not sure and refused
df["PHYSHLTH"] = df["PHYSHLTH"].replace({88: 0, 77: pd.NA, 99: pd.NA})

# 17 DIFFWALK
# change 2 to 0 for no. 1 is already yes
# remove 7 and 9 for don't know not sure and refused
df["DIFFWALK"] = df["DIFFWALK"].replace({1: "y", 2: "n", 7: pd.NA, 9: pd.NA})

# 18 SEX
# in other words - is respondent male (somewhat arbitrarily chose this change
# because men are at higher risk for heart disease)
# change 2 to 0 (female as 0). Male is 1
df["SEX"] = df["SEX"].replace(
    {
        1: "m",
        2: "f",
    }
)

# 19 _AGEG5YR
# already ordinal. 1 is 18-24 all the way up to 13 wis 80 and older. 5 year increments.
# remove 14 because it is don't know or missing
df["_AGEG5YR"] = df["_AGEG5YR"].replace(
    {
        1: "18-24",
        2: "25-29",
        3: "30-34",
        4: "35-39",
        5: "40-44",
        6: "45-49",
        7: "50-54",
        8: "55-59",
        9: "60-64",
        10: "65-69",
        11: "70-74",
        12: "75-79",
        13: "80+",
        14: pd.NA,
    }
)

# 20 EDUCA
# This is already an ordinal variable with 1 being never attended school or
# kindergarten only up to 6 being college 4 years or more
# Scale here is 1-6
# Remove 9 for refused:
df["EDUCA"] = df["EDUCA"].replace(
    {
        1: "no school",
        2: "elementary",
        3: "some high school",
        4: "high school graduate",
        5: "college",
        6: "college graduate",
        9: pd.NA,
    }
)

# 21 INCOME2
# Variable is already ordinal with 1 being less than $10,000 all the way up to 8 being $75,000 or more
# Remove 77 and 99 for don't know and refused
df["INCOME2"] = df["INCOME2"].replace(
    {
        1: "<$10k",
        2: "<$15k",
        3: "<$20k",
        4: "<$25k",
        5: "<$35k",
        6: "<$50k",
        7: "<$75k",
        8: ">$75k",
        77: pd.NA,
        88: pd.NA,
        99: pd.NA,
    }
)


df = df.rename(columns=new_column_names)

df.to_csv(
    os.path.join(DATA_RAW_DIR, DATA_RAW_FILENAME),
    index=False,
)
