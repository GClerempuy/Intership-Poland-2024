#!/bin/bash

#mkdir PlastidMitoPerLakes

# Fichier contenant la liste des noms de dossiers
export list_file="/home/clerempuy/ListLakeName.txt"

# Lire chaque ligne du fichier et créer un dossier
#while IFS= read -r folder_name; do
#  # Vérifier si le nom de dossier n'est pas vide
#  if [[ -n "$folder_name" ]]; then
#    # Créer le dossier
#    mkdir -p PlastidMitoPerLakes/"$folder_name"
#  fi
#done < "$list_file"

  

#python python_list_per_lake.py

export Largeur=60
export  fasta_file="/mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/"
export base_directory="/home/clerempuy/PlastidMitoPerLakes/" 

#Searche () {
#  echo $1
#  csv=$1
#  i=1
#  for element in $(awk -F',' 'NR>0 {print $1}' "$csv"); do
#    Len=$(awk -F',' -v line="$i" 'NR == line {print $2}' "$csv")
#    valeur_A=$(($Len / $Largeur))
#    zcat $fasta_file${element:0:16}* | grep -A"$valeur_A" "$element$" >> $dossier"${element:0:4}PM.fasta"

#    i=$((i+1))
#  done
    
#}

#export -f Searche

# Chemin vers le répertoire à parcourir
export repertoire="/home/clerempuy/PlastidMitoPerLakes"

# Parcourir les dossiers dans le répertoire
for dossier in "$repertoire"/*/; do
rm $dossier/*.fasta
    
done

export dossier="$repertoire"/*/

find '/home/clerempuy/PlastidMitoPerLakes/' -mindepth 1 -maxdepth 1 -type d | xargs -I {} -P 8 -n 1 bash -c '
  csv_file={}/*.csv
  i=1
  for element in $(awk -F"," "NR>0 {print $1}" $csv_file); do
    Len=$(awk -F"," -v line="$i" "NR==line {print $2}" $csv_file)
    valeur_A=$(($Len / $Largeur))
    zcat $fasta_file${element:0:16}* | grep -A"$valeur_A" "$element" >> $dossier"${element:0:4}PM.fasta"

    i=$((i+1))
  done
'

## Parcourir les dossiers dans le répertoire
#for dossier in "$repertoire"/*/; do
#csv_file=$dossier/*.csv
#Searche $csv_file &
    
#done


'/home/clerempuy/PlastidMitoPerLakes/' -mindepth 1 -maxdepth 1 -type d | xargs -I {} -P 8 -n 1 bash PlastidMito_one_folder.sh {}





