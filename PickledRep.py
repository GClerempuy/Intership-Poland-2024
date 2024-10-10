import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
import numpy as np
import pickle
import logging
import math
import os
import sys
from matplotlib.backends.backend_pdf import PdfPages
from drep.WorkDirectory import WorkDirectory
import scipy
from scipy.cluster.hierarchy import fcluster
import shutil


wd = WorkDirectory('/home/clerempuy/BinStat/dRep/')
Ndb = wd.get_db('Ndb', return_none=False)
Cdb = wd.get_db('Cdb', return_none=False)

base_path = '/home/clerempuy/BinStat'
output_dir = os.path.join("/home/clerempuy/BinStat/dRep/", 'GroupBin')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Lister tous les fichiers .fa disponibles
all_files = []
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".fa"):
            all_files.append(os.path.join(root, file))

print("There is", len(all_files)," bins files")

# Créer une liste pour stocker les fichiers déjà utilisés
used_files = []

file_count = 1

for cluster in sorted(Cdb['primary_cluster'].unique()):
    d = Cdb[Cdb['primary_cluster'] == cluster]
    # Skip if it's a singleton
    if len(d['genome'].unique()) == 1:
        continue
    # Load the linkage information
    linkI = wd.get_cluster("secondary_linkage_cluster_{0}".format(cluster))
    db = linkI['db']
    linkage = linkI['linkage']
    names = list(db.columns)
    n = len(names)
    threshold = 0.05
    assignments = fcluster(linkage, threshold, 'distance')
    cluster_output = pd.DataFrame({'Bins': names, 'cluster': assignments})
    cluster_groups = cluster_output.groupby('cluster')['Bins'].apply(list)
    for cluster, files in cluster_groups.items():
        group_name = f'GroupDREPX{file_count}.fa'
        group_path = os.path.join(output_dir, group_name)
        with open(group_path, 'wb') as output_file:
            for file in files:
                # Extraire les 4 lettres du lac et le premier nombre après ces lettres
                parts = file.split('_')
                lake_code = parts[1]  # Les 4 lettres
                first_number = parts[2]  # Le premier nombre (ici "12")
                # Construire le chemin en utilisant le nom du lac et le premier nombre
                subdir = f'{lake_code}_{first_number}'
                input_file_path = os.path.join(base_path, f'{lake_code}_BIN', 'bin_by_bin', f'Bin_{subdir}', file)
                if os.path.exists(input_file_path):
                    with open(input_file_path, 'rb') as input_file:
                        shutil.copyfileobj(input_file, output_file)
                    # Ajouter le fichier utilisé à la liste
                    used_files.append(input_file_path)
                else:
                    print(f"Fichier non trouvé: {input_file_path}")
        file_count += 1
        #print(f"Les fichiers ont été regroupés et sauvegardés dans {output_dir}")
        #a = input()#To do it one by one, delete #


# Ajouter les fichiers non utilisés à GroupBin
unused_file_count = 1
for file_path in all_files:
    if file_path not in used_files:
        unused_group_name = f'UnusedGroupDREPX{unused_file_count}.fa'
        unused_group_path = os.path.join(output_dir, unused_group_name)
        shutil.copy(file_path, unused_group_path)
        unused_file_count += 1

#print(f"Les fichiers ont été regroupés et sauvegardés dans {output_dir}")



