#!/bin/bash

#mkdir PlastidMitoPerLakes

# Fichier contenant la liste des noms de dossiers
list_file="/home/clerempuy/ListLakeName.txt"

# Lire chaque ligne du fichier et cr�er un dossier
#while IFS= read -r folder_name; do
#  # V�rifier si le nom de dossier n'est pas vide
#  if [[ -n "$folder_name" ]]; then
#    # Cr�er le dossier
#    mkdir -p PlastidMitoPerLakes/"$folder_name"
#  fi
#done < "$list_file"

  

python python_list_per_lake.py

Largeur=60
fasta_file="/mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/"
base_directory="/home/clerempuy/PlastidMitoPerLakes/" 

Searche () {

  csv=$1
  i=1
  for element in $(awk -F',' 'NR>0 {print $1}' "$csv"); do
    Len=$(awk -F',' -v line="$i" 'NR == line {print $2}' "$csv")
    valeur_A=$(($Len / $Largeur))
    zcat $fasta_file${element:0:16}* | grep -A"$valeur_A" "$element$" >> $dossier/"${element:0:4}PM.fasta"

    i=$((i+1))
  done
    
}


# Chemin vers le r�pertoire � parcourir
repertoire="/home/clerempuy/PlastidMitoPerLakes"

# Parcourir les dossiers dans le r�pertoire
for dossier in "$repertoire"/*/; do
rm $dossier/*.fasta
    
done



# Parcourir les dossiers dans le r�pertoire
for dossier in "$repertoire"/*/; do
csv_file=$dossier/*.csv
Searche $csv_file &
done



