# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:34:37 2024

@author: guush
"""

import csv

# Open het tekstbestand
with open('Data\posities\posities_1_Team_07.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    
    # Schrijf naar het CSV-bestand
    with open('Data\posities\posities_1_Team_07.txt', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
