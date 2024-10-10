#!/bin/bash

# Repertory
all_mappings_dir="/home/clerempuy/pelagics_plastids/all_mappings/"
pelagics_plastids_dir="/home/clerempuy/pelagics_plastids/"

# Extract name of file without extension
all_mappings_files=($(ls ${all_mappings_dir}*.tar.gz | xargs -n 1 basename | sed 's/_mapped.tar.gz//'))
pelagics_plastids_dirs=($(ls -d ${pelagics_plastids_dir}*_mapped | xargs -n 1 basename | sed 's/_mapped//'))

declare -A all_mappings_set
for file in "${all_mappings_files[@]}"; do
    all_mappings_set["$file"]=1
done

declare -A pelagics_plastids_set
for dir in "${pelagics_plastids_dirs[@]}"; do
    pelagics_plastids_set["$dir"]=1
done

# Find same names
echo "XXXX communs dans les deux r�pertoires :"
for file in "${all_mappings_files[@]}"; do
    if [[ -n "${pelagics_plastids_set[$file]}" ]]; then
        echo "$file"
    fi
done

# Find the lakes unique to all mapping_dir
echo "XXXX uniquement dans all_mappings_dir :"
for file in "${all_mappings_files[@]}"; do
    if [[ -z "${pelagics_plastids_set[$file]}" ]]; then
        echo "$file"
    fi
done

# Find the lakes unique to all pelagics_plastids_dir
echo "XXXX uniquement dans pelagics_plastids_dir :"
for dir in "${pelagics_plastids_dirs[@]}"; do
    if [[ -z "${all_mappings_set[$dir]}" ]]; then
        echo "$dir"
    fi
done
