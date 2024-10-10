#!/bin/bash
source /home/clerempuy/miniconda3/etc/profile.d/conda.sh
conda activate anvio-8

mkdir -p BinStat
cd /home/clerempuy/BinStat/
#Extract data from binning
while IFS= read -r file; do
  anvi-summarize -p /home/clerempuy/pelagics_plastids/${file:0:4}_mapped/SAMPLES-MERGED/PROFILE.db -c /home/clerempuy/pelagics_plastids/${file:0:4}_mapped/${file:0:4}.db -C ${file:0:4}_BIN -o /home/clerempuy/BinStat/${file:0:4}_BIN
done < /home/clerempuy/pelagics_plastids/Okfile.txt

cd /home/clerempuy
conda deactivate


####ChangeName####


while IFS= read -r file; do
  base_dir="/home/clerempuy/BinStat/${file:0:4}_BIN/bin_by_bin"
  LenRep=$(find "$base_dir" -maxdepth 1 -type d | wc -l)
  
  # Start counting
  count=1
  for dir in "$base_dir"/Bin_*; do
    if [ -d "$dir" ]; then
      new_dir="${base_dir}/Bin_${file:0:4}_${count}"
      
      # Renamme directory
      mv "$dir" "$new_dir"
      
      # Renamme files
      for old_file in "$new_dir"/*; do
        if [ -f "$old_file" ]; then
          base_name=$(basename "$old_file")
          new_file="${new_dir}/Bin_${file:0:4}_${count}_${base_name#*_}"
          mv "$old_file" "$new_file"
        fi
      done
      count=$((count + 1))
    fi
  done
done < /home/clerempuy/pelagics_plastids/Okfile.txt

echo "Done"