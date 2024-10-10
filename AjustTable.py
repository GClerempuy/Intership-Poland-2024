# -*- coding: utf-8 -*-
import pandas as pd

# read CSV file
df = pd.read_csv("Table.csv", sep="\t")
df.dropna(inplace=True)
# Split part of name
df['Assembly'] = df['Assembly'].apply(lambda x: x.split('.')[0])

# read the second CSV file
df2 = pd.read_csv("Table2.1.csv", sep=",")

# Split part of name
df2['Fichier'] = df2['Fichier'].apply(lambda x: x.split('_out_')[1].split('.txt')[0])
df2 = df2.rename(columns={"Fichier": "Assembly"})

merged_df = pd.merge(df, df2, on="Assembly")

# Create the new table
merged_df.to_csv("TableFinal.csv", index=False)





#####L50 means from initial data#####
"""
import pandas as pd
import glob

total_L50 = 0
count_L50 = 0

# Search transposed_report.txt in all repertory
for file in glob.glob('/home/clerempuy/quast_results/*/transposed_report.tsv'):
  df = pd.read_csv(file, sep="\t", header=0)
  # take L50
  L50_values = pd.to_numeric(df['L50'], errors='coerce')
  total_L50 += L50_values.sum()
  count_L50 += L50_values.count()

# print results
if count_L50 > 0:
    average_L50 = total_L50 / count_L50
    print(f"L50 mean : {average_L50:.2f}")
else:
    print("No L50 Find.")
"""