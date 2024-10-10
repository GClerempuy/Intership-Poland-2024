#!/bin/bash

# Convert backspace from windows to linux
sed -i 's/\r//' AnvioInterface.sh

# Check for number of argument
if [ "$#" -ne 1 ]; then
  echo "Error: Input should be a 4 letter format"
  exit 1
fi

#Input
XXXX="$1"

# Activate conda env
source /home/clerempuy/miniconda3/etc/profile.d/conda.sh
conda activate anvio-8


anvi-interactive -p /home/clerempuy/pelagics_plastids/${XXXX}_mapped/SAMPLES-MERGED/PROFILE.db -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db --server-only -P 8080

conda deactivate