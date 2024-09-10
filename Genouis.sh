#!/bin/bash
#geneious --options-for De_Novo_Assemble --filter "Log"

#Report option results.saveReport True
#Reads option results.saveUnusedReads true

#geneious -i "LOCAL:Dowload/AMAD/" --operation De_Novo_Assemble -o "C:/Users/clere/OneDrive/Bureau/Genius/AMADOutput.geneious"



#geneious -i "LOCAL:Dowload/AMAD/" --operation De_Novo_Assemble  --options "results.saveReport=true" "results.saveUnusedReads=true" -o "C:/Users/clere/OneDrive/Bureau/Genius/AMADOutput.geneious"

# Path to the CSV file containing folder names
CSV_FILE="C:\Users\clere\OneDrive\Bureau\Dowload\ListLakeName.txt"

# Read each line in the CSV file
while IFS=, read -r folder_name; do
    # Skip the header line if present
    if [ "$folder_name" == "Nom" ]; then
        continue
    fi

    # Construct the input and output paths
    input_path="LOCAL:Dowload/${folder_name}/"
    #output_path="C:/Users/clere/OneDrive/Bureau/Genius/${folder_name}Output.geneious"
    output_path="LOCAL:Dowload/OutPut/${folder_name}Out.geneious"

    # Execute the Geneious command
    geneious -i "$input_path" --operation De_Novo_Assemble --options "results.saveReport=true" "results.saveUnusedReads=true" -o "$output_path"
    #geneious -i "$input_path" --operation De_Novo_Assemble --options "results.saveReport=true" "results.saveUnusedReads=true" "results.generateConsensusSequencesDeNovo=true" "results.consensus.consensusSource=generateFromContig" -o "$output_path"

done < "$CSV_FILE"