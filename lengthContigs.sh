#!/bin/bash

# Fonction pour afficher l'aide
function show_help {
  echo "Usage: $0 -i <fichier1.fasta> <fichier2.fasta> ... [-h]"
  echo
  echo "Options:"
  echo "  -i, --input    Chemin vers les fichiers FASTA (peut être multiple)"
  echo "  -h, --help     Afficher l'aide"
  echo
  echo "La sortie sera formatée comme suit:"
  echo "nom_fichier;Total_length;number_of_contigs;Average_length"
  echo
  echo "où:"
  echo "  nom_fichier      est le nom du fichier FASTA"
  echo "  Total_length     est la longueur totale des contigs"
  echo "  number_of_contigs est le nombre de contigs"
  echo "  Average_length   est la longueur moyenne des contigs"
}

# Vérification des arguments
if [ $# -eq 0 ]; then
  show_help
  exit 1
fi

# Traitement des arguments
files=()
while getopts ":hi:" opt; do
  case ${opt} in
    i )
      IFS=' ' read -r -a files <<< "$OPTARG"
      ;;
    h )
      show_help
      exit 0
      ;;
    \? )
      echo "Option invalide: $OPTARG" 1>&2
      show_help
      exit 1
      ;;
    : )
      echo "L'option -$OPTARG nécessite un argument." 1>&2
      show_help
      exit 1
      ;;
  esac
done
shift $((OPTIND -1))

# Vérifiez si des fichiers sont fournis
if [ ${#files[@]} -eq 0 ]; then
  echo "Erreur: Aucun fichier FASTA fourni."
  show_help
  exit 1
fi

# Traitement de chaque fichier FASTA
for fasta_file in "${files[@]}"; do
  awk -v file_name="$(basename "$fasta_file")" '
    BEGIN {total_length=0; num_contigs=0;}
    /^>/ {if (seq_length) {total_length += seq_length; num_contigs++;} seq_length=0; next;}
    {seq_length += length($0);}
    END {
      if (seq_length) {total_length += seq_length; num_contigs++;}
      if (num_contigs > 0) {
        average_length = total_length / num_contigs;
        print file_name ";" total_length ";" num_contigs ";" average_length;
      } else {
        print file_name ";0;0;0";
      }
    }
  ' "$fasta_file"
done
