#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download the Behavioral Risk Factor Surveillance System (BRFSS) dataset from Kaggle
and transform it into a format suitable for analysis.
"""

import os
import subprocess
from config import DATA_SKRIPTS_DIR

# Download and transform the dataset
# This assumes that the Kaggle API is configured and the kaggle.json file is in place
# See the download_data.py file for the expected location of kaggle.json.
subprocess.run(["python", os.path.join(DATA_SKRIPTS_DIR, "download_data.py")])
subprocess.run(["python", os.path.join(DATA_SKRIPTS_DIR, "transform_data.py")])
