# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:33:21 2024

@author: guush
"""

import pandas as pd

# Define the file path
file_path = r'\Data\posities\posities_1_Team_07.txt'

# Read the txt file as csv
data = pd.read_csv(file_path, sep="\t")  # assuming the data is tab-separated

# Now 'data' is a pandas DataFrame and you can perform operations on it.
print(data)