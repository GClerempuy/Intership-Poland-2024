#!/bin/bash


# Spécifiez le répertoire contenant les fichiers compressés
repertoire="/mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/"

# Spécifiez le nom du fichier de sortie CSV
output_csv="LongueurContigs.csv"

# Parcourez tous les fichiers du répertoire
for fichier_compress in "$repertoire"/*; do
    # Extraire le nom de fichier sans extension
    nom_fichier=$(basename "$fichier_compress")
    # Décompressez le fichier et construisez l'index .fai
    gunzip -c "$fichier_compress" | samtools faidx -o Output - 
    cat Output >> "$output_csv"
    rm Output
done




python AllIDPlastidMitochondrion.py




#!/bin/bash

  tail -n +2 AllPlastidMitochondrion_length.csv > AllPlastidMitochondrion_length0.csv
  
  fasta_file="/mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/"
  csv_file="AllPlastidMitochondrion_length0.csv"
  
  
  
  # Lire le fichier CSV ligne par ligne et afficher chaque élément de la première colonne
  
  rm AllPlastidMitochondrion.fasta 
  touch AllPlastidMitochondrion.fasta 
  
  i=1
  Largeur=60
  for element1 in $(awk -F',' 'NR>0 {print $1}' "$csv_file"); do
      Len=$(awk -F',' -v line="$i" 'NR == line {print $5}' "$csv_file")
      valeur_A=$((Len / Largeur))
      zcat $fasta_file${element1:0:16}* | grep -A"$valeur_A" "$element1$" >> tmp/"$element1$".fasta
      i=$((i+1))
  done


#${element1:0:16}



i=1
for element1 in $(awk -F',' 'NR>0 {print $1}' "$csv_file"); do
Len=$(awk -F',' -v line="$i" 'NR == line {print $5}' "$csv_file")
valeur_A=$((Len / Largeur))
zcat $fasta_file${element1:0:16}* | grep -A"$valeur_A" "$element1$" >> tmp/"$element1$".fasta

if [ $((i % 1000)) -eq 0 ]; then
# Group all previous outputs into a single file
cat tmp/*.fasta > "${output_base}${i}.fasta"

# Compress the resulting file
gzip "tmp/${output_base}${i}.fasta"
# Remove individual fasta files
rm tmp/*.fasta

fi
    i=$((i+1))
done



