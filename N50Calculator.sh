#!/bin/bash

# Fonction to calculate N50 
calculate_n50() {
    lengths=("$@")
    total_length=0
    for len in "${lengths[@]}"; do
        total_length=$((total_length + len))
    done
    half_total=$((total_length / 2))

    lengths_sorted=($(printf '%s\n' "${lengths[@]}" | sort -nr))

    cumulative_length=0
    for len in "${lengths_sorted[@]}"; do
        cumulative_length=$((cumulative_length + len))
        if [ $cumulative_length -ge $half_total ]; then
            echo $len
            return
        fi
    done
}

# Fonction to make the mean of N50
calculate_mean_n50() {
    total_n50=0
    file_count=0

    for fasta_file in "$@"; do
        contig_lengths=()
        while read -r line; do
            if [[ $line == ">"* ]]; then
                if [ -n "$seq" ]; then
                    contig_lengths+=(${#seq})
                fi
                seq=""
            else
                seq+="$line"
            fi
        done < "$fasta_file"
        
        if [ -n "$seq" ]; then
            contig_lengths+=(${#seq})
        fi

        if [ ${#contig_lengths[@]} -gt 0 ]; then
            n50=$(calculate_n50 "${contig_lengths[@]}")
            total_n50=$((total_n50 + n50))
            file_count=$((file_count + 1))
            echo "Fichier: $fasta_file, N50: $n50"
        fi
    done

    if [ $file_count -gt 0 ]; then
        mean_n50=$((total_n50 / file_count))
        echo "N50 moyen de tous les fichiers: $mean_n50"
    else
        echo "Aucun fichier fasta trouv� ou aucun contig d�tect�."
    fi
}

# Check if file are valid input
if [ $# -eq 0 ]; then
    echo "Usage: $0 chemin_vers_fichiers"
    echo "Exemple: $0 /home/clerempuy/Genius/*/*PlastidG.fasta"
    exit 1
fi

calculate_mean_n50 "$@"
