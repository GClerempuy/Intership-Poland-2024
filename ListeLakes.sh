
cd /home/clerempuy/

### To obtain List of Lakes ID
ls -1 /mnt/archive/Cicuta_serwer/pelagics_assemblies_complete | cut -c 1-4 | sort | uniq > ListLakeName.txt


### To obtain numbers of data on a Lake
rm DataNumberPerLake.txt
longueur=$(wc -l < ListLakeName.txt)
for i in $(seq 1 $longueur); do     
result=$(find /mnt/archive/Cicuta_serwer/pelagics_assemblies_complete/ -type f -name "*$(head -n $i ListLakeName.txt | tail -n 1)*" | wc -l);     
echo "$(head -n $i ListLakeName.txt | tail -n 1)* : $result" >> DataNumberPerLake.txt; 
done