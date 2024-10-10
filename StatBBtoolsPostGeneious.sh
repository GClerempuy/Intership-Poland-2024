#!/bin/bash

# Parcourir chaque sous-dossier dans /home/clerempuy/Genius/
for dir in /home/clerempuy/Genius/*/; do
    # Supprimer les fichiers ne contenant pas "Consensus Sequences", "Unused Reads" ou "Report"
    find "$dir" -type f ! -name "*Consensus Sequences*" ! -name "*Unused Reads*" ! -name "*Report*" -exec rm -f {} +

    # Définir les chemins des fichiers Consensus et Unused Reads
    consensus_file=$(find "$dir" -type f -name "*Consensus Sequences*")
    unused_file=$(find "$dir" -type f -name "*Unused Reads*")

    # Vérifier si les fichiers existent
    if [[ -f "$consensus_file" && -f "$unused_file" ]]; then
        # Assembler les fichiers fasta
        cat "$consensus_file" "$unused_file" > "$dir/Output.fasta"

        # Exécuter bbmap/bbstats.sh
        bbmap/bbstats.sh in="$dir/Output.fasta" > "$dir/bbtoolsOut.txt"
    fi
done


# Fichier de sortie CSV
output_csv="/home/clerempuy/Genius/results.csv"

# En-tête du fichier CSV
echo "nom;valeur" > "$output_csv"

# Créer une liste des résultats pour tous les fichiers bbtoolsOut.txt
for output_file in /home/clerempuy/Genius/*/bbtoolsOut.txt; do
    # Extraire le nom du répertoire parent
    dir_name=$(basename "$(dirname "$output_file")")

    # Extraire la valeur correspondant à "10 KB"
    value=$(grep -P '^\s*10 KB' "$output_file" | awk '{print $3}')

    # Ajouter la ligne au fichier CSV
    echo "$dir_name;$value" >> "$output_csv"
done


# Parcourir tous les répertoires sous /home/clerempuy/Genius/
for dir in /home/clerempuy/Genius/*/; do
    # Vérifier si le fichier Output.fasta existe dans le répertoire
    if [[ -f "$dir/Output.fasta" ]]; then
        # Extraire le nom du répertoire parent
        dir_name=$(basename "$dir")
        
        # Renommer le fichier Output.fasta en XXXXPlastidG.fasta
        mv "$dir/Output.fasta" "$dir/${dir_name}PlastidG.fasta"
        
        # Afficher le renommage
        echo "Renommé $dir/Output.fasta en $dir/${dir_name}PlastidG.fasta"
    fi
done


# Parcourir tous les répertoires sous /home/clerempuy/Genius/
for dir in /home/clerempuy/Genius/*/; do
    # Définir les noms des fichiers
    input_file="${dir}$(basename "$dir")PlastidG.fasta"
    output_file="${dir}$(basename "$dir")PlastidG10000.fasta"
    
    # Vérifier si le fichier d'entrée existe
    if [[ -f "$input_file" ]]; then
        # Initialiser les variables pour awk
        in_contig=0
        contig_length=0
        contig_header=""
        contig_sequence=""
        
        # Utiliser awk pour extraire les contigs > 10 000 pb
        awk '
        /^>/ {
            if (contig_length > 10000) {
                print contig_header >> output_file
                print contig_sequence >> output_file
            }
            contig_header = $0
            contig_length = 0
            contig_sequence = ""
        }
        /^[^>]/ {
            contig_length += length($0)
            contig_sequence = contig_sequence $0
        }
        END {
            if (contig_length > 10000) {
                print contig_header >> output_file
                print contig_sequence >> output_file
            }
        }
        ' output_file="$output_file" "$input_file"
        
        # Afficher un message pour chaque fichier traité
        echo "Contigs > 10 000 pb extraits de $input_file vers $output_file"
    else
        echo "Fichier $input_file non trouvé."
    fi
done

output_csv="/home/clerempuy/Genius/results.csv"

# En-tête du fichier CSV
echo "nom;10KB;50KB;100KB" > "$output_csv"

# Créer une liste des résultats pour tous les fichiers bbtoolsOut.txt
for output_file in /home/clerempuy/Genius/*/bbtoolsOut.txt; do
    # Extraire le nom du répertoire parent
    dir_name=$(basename "$(dirname "$output_file")")

    # Extraire les valeurs correspondantes
    value_10kb=$(grep -P '^\s*10 KB' "$output_file" | awk '{print $3}')
    value_50kb=$(grep -P '^\s*50 KB' "$output_file" | awk '{print $3}')
    value_100kb=$(grep -P '^\s*100 KB' "$output_file" | awk '{print $3}')

    # Ajouter la ligne au fichier CSV
    echo "$dir_name;$value_10kb;$value_50kb;$value_100kb" >> "$output_csv"
done



















# Répertoire cible
TARGET_DIR="/home/clerempuy/Dowload/*"

# Parcourir chaque sous-dossier dans /home/clerempuy/Genius/
for dir in /home/clerempuy/Dowload/*; do

    # Exécuter bbmap/bbstats.sh
    bbmap/bbstats.sh in=$TARGET_DIR/* > "$TARGET_DIR/bbtoolsOut.txt"

done



