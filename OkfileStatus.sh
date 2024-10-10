#!/bin/bash

# Path
BASE_DIR="/home/clerempuy/pelagics_plastids"
OKFILE="$BASE_DIR/Okfile.txt"

# Reads the XXXX in Okfile.txt
okfile_XXXX=$(cat "$OKFILE")

# Extract XXXX in repertory XXXX_mapped
folder_XXXX=$(ls -d $BASE_DIR/*_mapped | sed -e 's#.*/##' -e 's/_mapped//')

# Compare the XXXX and give the list of the one not in Okfile.txt
for folder in $folder_XXXX; do
  if ! grep -q "$folder" <<< "$okfile_XXXX"; then
    echo "$folder"
  fi
done

#Okfile should be add manualy after finishing a bin