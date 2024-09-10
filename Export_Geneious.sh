#!/bin/bash

#Export_to_Multiple_Files


CSV_FILE="C:\Users\clere\OneDrive\Bureau\Dowload\ListLakeName.txt"

# Read each line in the CSV file
while IFS=, read -r folder_name; do
    # Skip the header line if present
    if [ "$folder_name" == "Nom" ]; then
        continue
    fi

    # Construct the input and output paths
    input_path_Consensus="LOCAL:Dowload/OutPut/${folder_name}Out.geneious/"
    
    output_path_Consensus="C:/Users/clere/OneDrive/Bureau/Genius/${folder_name}/${folder_name}.fasta"
    #Create Folder

    mkdir "C:/Users/clere/OneDrive/Bureau/Genius/${folder_name}"

    # Execute the Geneious command
    
    geneious --multi-file --input "$input_path_Consensus" --output "$output_path_Consensus" 

done < "$CSV_FILE"


#"LOCAL:Dowload/OutPut/AMADOut.geneious/Assembly Consensus Sequences"
scp -r C:\Users\clere\OneDrive\Bureau\Genius clerempuy@212.87.6.112:/home/clerempuy/
