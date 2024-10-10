### Creates repertory And do quast
for i in $(seq 1 $longueur); do 
find /mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/ -type f -name "$(head -n $i /home/clerempuy/ListLakeName.txt | tail -n 1)*" > /home/clerempuy/List_$(head -n $i /home/clerempuy/ListLakeName.txt | tail -n 1).txt
xargs quast.py --fast -t 25 -o quast_results/$(head -n $i /home/clerempuy/ListLakeName.txt | tail -n 1) < /home/clerempuy/List_"$(head -n $i /home/clerempuy/ListLakeName.txt| tail -n 1)".txt
done