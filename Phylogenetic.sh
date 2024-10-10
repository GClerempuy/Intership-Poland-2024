mkdir Phylo
cd Phylo
cat /home/clerempuy/rbcL_gene_extraction.fasta /home/karlicki/rbcl_2/rbcL_final.fa  > /home/clerempuy/Phylo/rbcLtoRun.fasta
/home/clerempuy/mafft-linux64/mafft.bat --thread 10 /home/clerempuy/Phylo/rbcLtoRun.fasta > /home/clerempuy/Phylo/rbcL_Mafft_output.fa
/home/clerempuy/trimal/source/trimal -in /home/clerempuy/Phylo/rbcL_Mafft_output.fa -gt 0.3 -st 0.001 -out /home/clerempuy/Phylo/trimmed_mafft_aln_rbcL_final.fa
awk '/^>/{print $0"_"++i; next}1' /home/clerempuy/Phylo/trimmed_mafft_aln_rbcL_final.fa > /home/clerempuy/Phylo/trimmed_mafft_aln_rbcL_final2.fa
raxml-ng --all --msa /home/clerempuy/Phylo/trimmed_mafft_aln_rbcL_final2.fa --model HKY+G4 --tree pars{25} --bs-trees 100 -threads 30 --workers 6