#!/bin/bash

# Repertory
REPERTOIRE=${1:-.}

# output file
FICHIER_SORTIE="ListScript.txt"

# find file with extension .sh et .py 
echo "Recherche des fichiers .sh et .py dans le r�pertoire: $REPERTOIRE (sans sous-dossiers)"
find "$REPERTOIRE" -maxdepth 1 \( -name "*.sh" -o -name "*.py" \) > "$FICHIER_SORTIE"

# Print ending indication
echo "R�sultats enregistr�s dans le fichier : $FICHIER_SORTIE"
