#!/bin/bash

# Adjuste backspace
sed -i 's/\r//' binAdapt.sh

if [ "$#" -ne 2 ]; then
  echo "Error : Please give two arguments : 4 letters and a bin num."
  exit 1
fi

XXXX=$1
bin=$2

if [[ ! "$XXXX" =~ ^[A-Za-z]{4}$ ]]; then
  echo "Error : Check the 4 letter you give, something goes wrong."
  exit 1
fi

# Activate conda env
source /home/clerempuy/miniconda3/etc/profile.d/conda.sh
conda activate anvio-8

anvi-refine -p /home/clerempuy/pelagics_plastids/${XXXX}_mapped/SAMPLES-MERGED/PROFILE.db -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db -C ${XXXX}_BIN -b Bin_${bin} -P 8080

conda deactivate