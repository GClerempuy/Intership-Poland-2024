#!/bin/bash


mkdir -p /home/clerempuy/Quast_Plastid


repertoire="/home/clerempuy/Genius"


for fichier in "$repertoire"/*; do
  nom_fichier=$(basename "$fichier")
  mkdir -p /home/clerempuy/Quast_Plastid/$nom_fichier
  
  
  file=`find "$fichier" -name "*Consensus*"`
  
  python RetourLigne.py -i "$file" -o /home/clerempuy/Quast_Plastid/$nom_fichier/$nom_fichier"_Consensus.fasta"
  python /home/clerempuy/miniconda3/bin/quast.py -m 0 -t 10 -o /home/clerempuy/Quast_Plastid/"$nom_fichier"/"$nom_fichier"_Consensus /home/clerempuy/Quast_Plastid/"$nom_fichier"/"$nom_fichier"_Consensus.fasta
  
  

  file=`find "$fichier" -name "*Unused*"` 
  
  python RetourLigne.py -i "$file" -o /home/clerempuy/Quast_Plastid/$nom_fichier/$nom_fichier"_Unused.fasta"
  python /home/clerempuy/miniconda3/bin/quast.py -m 0 -t 10 -o /home/clerempuy/Quast_Plastid/"$nom_fichier"/"$nom_fichier"_Unused /home/clerempuy/Quast_Plastid/"$nom_fichier"/"$nom_fichier"_Unused.fasta
done



#python /home/clerempuy/miniconda3/bin/quast.py -o /home/clerempuy/Quast_Plastid/"$nom_fichier"Unused /home/clerempuy/Quast_Plastid/"$nom_fichier"/"$nom_fichier"_Consensus.fasta


#/home/clerempuy/miniconda3/bin/quast.py --fast -t 25 -o /home/clerempuy/Quast_Plastid/$nom_fichier/$nom_fichier"Unused"