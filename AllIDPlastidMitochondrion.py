# -*- coding: utf-8 -*-
import os
import pandas as pd

donnees = []

# Path repertory
chemin_repertoire = '/home/clerempuy/Tiara_results/'

# List of file contening the caracter chain "Tiara_out"
fichiers_tiara_out = []

for nom_fichier in os.listdir(chemin_repertoire):
    # Check if the name start with "Tiara_out"
    if nom_fichier.startswith("Tiara_out"):
        # Add complete path to the list
        fichiers_tiara_out.append(os.path.join(chemin_repertoire, nom_fichier))
        
        
        
for fichier in fichiers_tiara_out:
    with open(fichier, 'r') as f:
        contenu = f.read()
        contenu = contenu.split('\n')  # remove empty line
        for ligne in contenu:
            if ligne:  # Check if the line is empty
                colonnes = ligne.split('\t')
                donnees.append(colonnes)

# Create a new dataframe from data (donnees in french)
nouveau_dataframe = pd.DataFrame(donnees)
nouveau_dataframe = nouveau_dataframe.fillna('None')
    
# Write all results
plastid_rows = nouveau_dataframe[nouveau_dataframe[2].str.contains('plastid', case=False)]
mitochondrion_rows = nouveau_dataframe[nouveau_dataframe[2].str.contains('mitochondrion', case=False)]

merged_df = pd.concat([plastid_rows, mitochondrion_rows])


Longueur = pd.read_csv("LongueurContigs.csv", sep="\t")
Longueur.drop(columns=[Longueur.columns[4], Longueur.columns[2], Longueur.columns[3]])

merged_final = pd.merge(merged_df, Longueur, left_on=merged_df.columns[0], right_on=Longueur.columns[0], how='inner')
merged_final.to_csv('AllPlastidMitochondrion_length.csv', index=False)  

merged_df.to_csv('AllPlastidMitochondrion.csv', index=False)
print(merged_final)










































"""               
#for i in range(1,len(contenu)):        
contenu['class_snd_stage'] = contenu['class_snd_stage'].fillna('None')
plastid_rows = contenu[contenu['class_snd_stage'].str.contains('plastid', case=False)]
mitochondrion_rows = contenu[contenu['class_snd_stage'].str.contains('mitochondrion', case=False)]
donnees.append(plastid_rows)
donnees.append(mitochondrion_rows)      
nouveau_dataframe = pd.DataFrame(donnees)
print(nouveau_dataframe)
"""