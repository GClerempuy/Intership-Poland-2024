#import pandas as pd
#import os

#csv_file = "AllPlastidMitochondrion_length0.csv"
#base_directory = "/home/clerempuy/PlastidMitoPerLakes/"

# V�rifier si le fichier CSV existe
#if not os.path.isfile(csv_file):
#    print(f"Le fichier {csv_file} n'existe pas.")
#    exit(1)

# Lire la premi�re colonne du fichier CSV
#df = pd.read_csv(csv_file)
#first_column = df.iloc[:, 0]

#for folder in os.listdir(base_directory):
#    folder_path = os.path.join(base_directory, folder)
#    if os.path.isdir(folder_path):
#        match_file = os.path.join(folder_path, f"{folder}_matches.csv")
#        # Supprimer le fichier de correspondance s'il existe
#        if os.path.isfile(match_file):
#            os.remove(match_file)


#print("Suppression des fichiers termin�e.")

# Parcourir chaque nom dans la premi�re colonne
#for name in first_column:
#    # V�rifier si le nom de dossier correspondant existe
#    for folder in os.listdir(base_directory):
#        folder_path = os.path.join(base_directory, folder)
#        if os.path.isdir(folder_path) and folder in name:
#            # Si le dossier contient le nom, �crire le nom dans un fichier CSV dans ce dossier
#            match_file = os.path.join(folder_path, f"{folder}_matches.csv")
#            with open(match_file, 'a', newline='', encoding='utf-8') as match_csv:
#                match_csv.write(f"{name}\n")

#print("Extration of csv per lake done Beep Boop.")


import pandas as pd
import os

csv_file = "AllPlastidMitochondrion_length0.csv"
base_directory = "/home/clerempuy/PlastidMitoPerLakes/"

# V�rifier si le fichier CSV existe
if not os.path.isfile(csv_file):
    print(f"Le fichier {csv_file} n'existe pas.")
    exit(1)

# Lire la premi�re et la derni�re colonne du fichier CSV
df = pd.read_csv(csv_file, usecols=[0, 4])

# Boucle pour supprimer les fichiers de correspondance existants
for folder in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder)
    if os.path.isdir(folder_path):
        match_file = os.path.join(folder_path, f"{folder}_matches.csv")
        if os.path.isfile(match_file):
            os.remove(match_file)

print("Suppression des fichiers termin�e.")

# Parcourir chaque nom et longueur dans les colonnes s�lectionn�es
for index, row in df.iterrows():
    # V�rifier si le nom de dossier correspondant existe
    for folder in os.listdir(base_directory):
        folder_path = os.path.join(base_directory, folder)
        if os.path.isdir(folder_path) and folder in row[0]:
            # Si le dossier contient le nom, �crire les informations dans un fichier CSV dans ce dossier
            match_file = os.path.join(folder_path, f"{folder}_matches.csv")
            with open(match_file, 'a', newline='', encoding='utf-8') as match_csv:
                match_csv.write(f"{row[0]},{row[1]}\n")

print("Extration of csv per lake done Beep Boop.")
