#!/bin/bash
# !"£$%^&*()_"|/.,~

# folder=/home/clerempuy/PlastidMitoPerLakes/AMAD/
folder=$1
echo "Working on file "$folder

#Removing old fasta
rm $folder/*.fasta

csv_file=$folder/*.csv

list_file="/home/clerempuy/ListLakeName.txt"
Largeur=60
fasta_file="/mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/"
base_directory="/home/clerempuy/PlastidMitoPerLakes/" 

Searche () {
  csv=$1
  i=1
  for element in $(awk -F',' 'NR>0 {print $1}' "$csv"); do
    Len=$(awk -F',' -v line="$i" 'NR == line {print $2}' "$csv")
    valeur_A=$(($Len / $Largeur))

    zcat $fasta_file${element:0:16}* | grep -A"$valeur_A" "$element$" >> $folder/"${element:0:4}PM.fasta"

    i=$((i+1))
  done
}

Searche $csv_file