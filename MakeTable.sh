#!/bin/bash

output_file="/home/clerempuy/Table.csv"
input_file="/home/clerempuy/Merged_data.tsv"
# rm output of this script if it's already exist
rm -f "$output_file"

#Take column of interst
cut -f4,3,2,1,8,14,17,18,19,20 "$input_file" > "$output_file"

rm -f /home/clerempuy/tmp/Tabletmp.csv
rm -f /home/clerempuy/tmp/Tabletmp2.csv

echo "First part ended and put in $output_file."

python MakeTable2.py

sort /home/clerempuy/Table2.csv | uniq > /home/clerempuy/Table2.1.csv

python AjustTable.py

echo "Script ended and put in $output_file."