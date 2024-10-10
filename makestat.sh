# Output
output_file="MoyenneTaillePlastidPostGeneious.csv"

# header of the CSV file
echo "nom_fichier;Total_length;number_of_contigs;Average_length" > "$output_file"

for fasta_file in /home/clerempuy/Genius/*/*PlastidG.fasta; do
  ./lengthContigs.sh -i "$fasta_file" >> "$output_file"
done




output_file="MoyenneTaillePlastid10000PostGeneious.csv"

# Header of the CSV file
echo "nom_fichier;Total_length;number_of_contigs;Average_length" > "$output_file"

for fasta_file in /home/clerempuy/Genius/*/*PlastidG10000.fasta; do
  ./lengthContigs.sh -i "$fasta_file" >> "$output_file"
done