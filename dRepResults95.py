import pandas as pd
import os


output_dir = '/home/clerempuy/BinStat/dRep/GroupBin'
os.makedirs(output_dir, exist_ok=True)  # Create the repertory if it doesnt exist



data=pd.read_csv("/home/clerempuy/BinStat/dRep/data_tables/Ndb.csv", sep=",", header=0)
data = data[data['ani'] != 1]



ani95 = data[data['ani'] >= 0.95]
ani95_sorted = ani95.sort_values(by='reference')



unique1 = data['reference'].unique()
unique = sorted(unique1)

def group(UniqueGene, GroupNum):
    Group=[]
    Group.append(UniqueGene)
    Search = ani95_sorted[ani95_sorted['reference'] == UniqueGene]
    Group.append(Search['querry'].tolist())
    Group2 = [item for sublist in Group for item in (sublist if isinstance(sublist, list) else [sublist])]
    if len(Group2) >=2 :
      file_path = os.path.join(output_dir, f'Group{GroupNum}.txt')
      with open(file_path, 'w') as f:
          for item in Group2:
              f.write(f"{item}\n")

for i in range(0,len(unique)):
    group(unique[i], i+1)
    ani95_sorted = ani95_sorted[~ani95_sorted['reference'].str.contains(unique[i], na=False) & ~ani95_sorted['querry'].str.contains(unique[i], na=False)]



