# -*- coding: utf-8 -*-

import os
import re
import csv

# Path of tiara output log
log_directory = "/home/clerempuy/Tiara_results/"
output_csv = "/home/clerempuy/Table2.csv"

# Define header
columns = ["archaea", "bacteria", "eukarya", "organelle", "prokarya", "unknown", "mitochondrion", "plastid"]

# Fonction to extract the values from log files
def extract_values(log_file):
    values = {}
    with open(log_file, "r") as f:
        content = f.read()
        for col in columns:
            match = re.search(fr"{col}: (\d+)", content)
            if match:
                values[col] = match.group(1)
            else:
                values[col] = ""

    return values

# Write the csv output
with open(output_csv, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Fichier"] + columns)
    writer.writeheader()

    # Parcourir tous les fichiers de log dans le r�pertoire
    for log_file in os.listdir(log_directory):
        if log_file.startswith("log_") and log_file.endswith(".txt"):
            file_values = extract_values(os.path.join(log_directory, log_file))
            writer.writerow({"Fichier": log_file, **file_values})
            writer.writerow({"Fichier": log_file, **file_values})




