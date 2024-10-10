Hi! This is the global ReadMe for all scripts. 

I'm going to go into more detail here, giving you the Inputs, Outputs and tools I've used.





ListeLakes.sh

Description : This script go take all file's names and list them, it will also give you the number of file per Lakes.

Input : /mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/*
Output : ListLakeName.txt & DataNumberPerLake.txt
Tools : Just Bash.





Quast.sh

Description : This script create one reperitory per Lakes and will run quast on all files of this lake.

Input : /mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/* & ListLakeName.txt
Output : A repertory nammed like a lakes that contains :
                    - quast.log (information about quast run)
                    - report (in tex, tsv, txt) 
                    - transposed_report (in tex, tsv, txt)
Tools : Quast.py

Warning : The lakes RIMV has 80 files, it can don't run correctly, so check if all ok, or run it manually.





Merger_of_lakes_quast.sh

Description : Merge all quast as one file.

Input : Quast.sh output
Output : Merged_data.tsv
Tools : awk





Tiara.sh

Description : Run Tiara on all the file one by one.

Input : /mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/*
Output : log_Tiara_out_XXXXX-XM-Date.txt & Tiara_out_XXXXX-XM-Date.txt
Tools : Tiara

Warning : You need to have a Tiara env. If you don't see this : https://github.com/ibe-uw/tiara/blob/main/docs/detailed-installation.md





MakeTable.sh

Description : Make a resume table of data per lakes (Quast and Tiara)

Input : /home/clerempuy/Merged_data.tsv
Output : /home/clerempuy/Table.csv
Tools : MakeTable2.py & AjustTable.py

AjustTable.py : Correct the files and merge the data
MakeTable2.py : Take in the Tiara folder the data of each type in the log files



AjustTable.py

Description : Assemble intermedian table in the final one & containt a code to get all the L50 from quast output (need to be run in the good repertory)

Input: Table.csv & Table2.1.csv & /home/clerempuy/quast_results/*/transposed_report.tsv
output: TableFinal.csv



AllIDPlastidMitochondrion.py


Description : Take all contigs name identified as platid or Mitochondrion and add the length of the contigs to the table

Input : /home/clerempuy/Tiara_results/*/*Tiara_out*
Output : AllPlastidMitochondrion.csv & AllPlastidMitochondrion_length.csv
Tools : pandas





PlastidMitochondrion.sh

Description : Give the longueur of all contigs & Repare length file header

Input : /mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/* & AllPlastidMitochondrion_length.csv
Output : LongueurContigs.csv & AllPlastidMitochondrion_length0.csv
Tools : samtools faidx





python_list_per_lakes.py

Description : Collect the ID of lakes and the length in the file AllPlastidMitochondrion_length0.csv

Input : AllPlastidMitochondrion_length0.csv 
Output : {folder}_matches.csv
Tools : pandas & os





MakeDowloadForGenius.sh

Description : Copie Paste the files identified as Plastid & Mitochondrion.

Input : /home/clerempuy/PlastidMitoPerLakes/*/*
Output : /home/clerempuy/Dowload/*/*PM.fasta



AnvioConvert.py

Description : Adjust file header name for the mapping

Input : /home/clerempuy/ForMapping
Output : /home/clerempuy/ForMapping/*_renamed.fasta & /home/clerempuy/ForMapping/*.csv



AnvioRun.sh

Description : Create database use by anvi'O

Input : /home/clerempuy/pelagics_plastids/all_mappings/${XXXX}_mapped.tar.gz & /home/clerempuy/miniconda3/etc/profile.d/conda.sh & /home/karlicki/anvio_plastid_profiles/Green_lineage_HMM/ & /home/karlicki/anvio_plastid_profiles/Ochro_genes_HMM/
Output : /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db



FileRunedAnvio.sh

Description : Give the name of lakes without database created



AnvioInterface.sh

Description : Open the link to acces anvi'o from google chrome (ssh -L 8080:localhost:8080 clerempuy@212.87.6.112) 

Input : /home/clerempuy/miniconda3/etc/profile.d/conda.sh & /home/clerempuy/pelagics_plastids/${XXXX}_mapped/SAMPLES-MERGED/PROFILE.db -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db --server-only -P 8080
Output : /home/clerempuy/pelagics_plastids/${XXXX}_mapped/SAMPLES-MERGED/PROFILE.db -c /home/clerempuy/pelagics_plastids/${XXXX}_mapped/${XXXX}.db --server-only -P 8080



binAdapt.sh

Description : Open a bin and let you adjust it in google chrome (or others explorer)

Input:Lake letter, num of the bin
Output:None



BinStat.sh

Description: Extract bins data

Input: /home/clerempuy/pelagics_plastids/${file:0:4}_mapped/${file:0:4}.db & /home/clerempuy/pelagics_plastids/Okfile.txt
Output: /home/clerempuy/BinStat/${file:0:4}_BIN/*



BestN50Bins.py

Description : Give the best N50 cluster, and plot the heatmaps of presence abscence of cluster in lake

Input: /home/clerempuy/BinStat/dRep/GroupBin/contigs_summary.csv
Output: None



StatBBtoolsPostGeneious.sh

Description:

Input:
Output:



DiagSimple.py

Description: Create 2 Diagrame from the CSV ( Diagramme.csv & DiagrammeSimple.csv )

Input: Diagramme.csv & DiagrammeSimple.csv
Output: diagramSimple.png/pdf & diagram.png/pdf




dRepMerge.py : dRepMerge.py [-h] [-o OUTPUT_DIR] [-t THRESHOLD] wd bin_path

Description:Group bin with dRep respecting a threshold

Input: dRep file
Output: contigs_summary.csv, group_per_bins (repertory)



find_files.sh

Description : Find the script and save the name in a file

Input : Repertory 
Output : ListScript.txt



makestat.sh

Description: Give the length and the number of contigs after geneious Prime. It's not optimized, you should use Quast or BBstat. But for little test it's working.

Input: /home/clerempuy/Genius/*/*PlastidG.fasta & /home/clerempuy/Genius/*/*PlastidG10000.fasta
Output: MoyenneTaillePlastidPostGeneious.csv & MoyenneTaillePlastid10000PostGeneious.csv



N50Calculator.sh

Description: Calcul N50 from fasta files, if many are given, give also the mean

Input: Fasta file(s)
Output: N50 (N50 mean)



Phylogenetic.sh

Description: Create the phylogenetic tree from rbcl genes

Input: /home/clerempuy/rbcL_gene_extraction.fasta & /home/karlicki/rbcl_2/rbcL_final.fa
Output: raxml output (to plot tree)



PlastidMito_one_folder.sh

Description: Create the fasta file of mitochondrion and plastid (not the optimized one but it's work)

Input: /home/clerempuy/ListLakeName.txt & /mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/ & /home/clerempuy/PlastidMitoPerLakes/
Output: XXXXPM.fasta