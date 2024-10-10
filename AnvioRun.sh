#!/bin/bash

# Convert backspace from windows to linux
sed -i 's/\r//' AnvioRun.sh

# Check argument
if [ "$#" -ne 1 ]; then
  echo "Error:need input of 4 letter"
  exit 1
fi

XXXX="$1" #Input


# Activate conda env
source /home/clerempuy/miniconda3/etc/profile.d/conda.sh
conda activate anvio-8

# Extract mapping file : tar.gz
tar -xzf "/home/clerempuy/pelagics_plastids/all_mappings/${XXXX}_mapped.tar.gz" -C /home/clerempuy/pelagics_plastids

#Database
anvi-gen-contigs-database -f /home/clerempuy/ForMapping/${XXXX}PlastidG_renamed_modified.fasta.gz -o /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db -n '${XXXX}' --num-threads 5
anvi-run-hmms -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db --num-threads 5

anvi-run-hmms -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db -H /home/karlicki/anvio_plastid_profiles/Green_lineage_HMM/ -T 6 --num-threads 5
anvi-run-hmms -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db -H /home/karlicki/anvio_plastid_profiles/Ochro_genes_HMM/ -T 6 --num-threads 5
anvi-run-ncbi-cogs -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db --num-threads 5


for file in /home/clerempuy/pelagics_plastids/${XXXX}_mapped/*${XXXX}*.bam; do
anvi-profile -i $file -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db --num-threads 5
done

anvi-merge /home/clerempuy/pelagics_plastids/${XXXX}_mapped/*/PROFILE.db -o /home/clerempuy/pelagics_plastids/${XXXX}_mapped/SAMPLES-MERGED -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db 

# Deactivate conda env
conda deactivate
