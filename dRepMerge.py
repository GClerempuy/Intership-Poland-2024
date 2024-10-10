# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import argparse
import os
import logging
import shutil
import pandas as pd
from drep.WorkDirectory import WorkDirectory
from scipy.cluster.hierarchy import fcluster
import matplotlib.pyplot as plt
import seaborn as sns

def modify_contig_titles(input_file_path, output_file_path, prefix):
    #Modify contig titles by adding a prefix to each title and ensure proper formatting.
    with open(input_file_path, 'r', newline='\n') as input_file, open(output_file_path, 'w', newline='\n') as output_file:
        for line in input_file:
            if '>' in line:  # If it's a contig title line
                output_file.write(f">{prefix}{line[1:]}")  # Modify the title with lake name and contigs number
            else:
                output_file.write(line)  # Write the sequence

def main(wd, bin_path, output_dir, threshold):
    # Initialize logging
    output_dir = os.path.join(output_dir, 'GroupBin')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    logging.basicConfig(filename=os.path.join(output_dir, 'log.txt'), level=logging.INFO)

    wd = WorkDirectory(wd)
    Cdb = wd.get_db('Cdb', return_none=False)

    # List all the available .fa files
    all_files = []
    for root, dirs, files in os.walk(bin_path):
        for file in files:
            if file.endswith(".fa"):
                all_files.append(os.path.join(root, file))

    logging.info(f"There were {len(all_files)} bin files in total.")

    used_files = [] #Will be use to take last bins not in the secondary clustering
    file_count = 1

    for cluster in sorted(Cdb['primary_cluster'].unique()):
        d = Cdb[Cdb['primary_cluster'] == cluster]
        # Skip if it's a singleton just in case
        if len(d['genome'].unique()) == 1:
            continue

        # Load the linkage information
        linkI = wd.get_cluster(f"secondary_linkage_cluster_{cluster}")
        db = linkI['db']
        linkage = linkI['linkage']
        names = list(db.columns)
        Cut = (100 - threshold) / 100
        assignments = fcluster(linkage, t=Cut, criterion='distance') #Cut the dendrogram
        cluster_output = pd.DataFrame({'Bins': names, 'cluster': assignments})
        cluster_groups = cluster_output.groupby('cluster')['Bins'].apply(list)

        for cluster, files in cluster_groups.items():
            group_name = f'GroupDREPX{file_count}.fa'
            group_path = os.path.join(output_dir, group_name)
            with open(group_path, 'w') as output_file:
                for file in files:
                    parts = file.split('_')
                    lake_code = parts[1]
                    first_number = parts[2]
                    subdir = f'{lake_code}_{first_number}'
                    input_file_path = os.path.join(bin_path, f'{lake_code}_BIN', 'bin_by_bin', f'Bin_{subdir}', file)

                    if os.path.exists(input_file_path):
                        temp_file_path = os.path.join(output_dir, f'temp_{file}')
                        modify_contig_titles(input_file_path, temp_file_path, file[:-3])
                        with open(temp_file_path, 'r') as temp_file:
                            shutil.copyfileobj(temp_file, output_file)
                        used_files.append(input_file_path)
                        os.remove(temp_file_path)  # Clean up the temporary file
                    else:
                        logging.warning(f"File not found: {input_file_path}")

            file_count += 1

    # Add unused files to GroupBin
    unused_file_count = 1
    for file_path in all_files:
        if file_path not in used_files:
            unused_group_name = f'UnusedGroupDREPX{unused_file_count}.fa'
            unused_group_path = os.path.join(output_dir, unused_group_name)
            pref = file_path.rfind('/')
            substring = file_path[pref + 1:-3]
            modify_contig_titles(file_path, unused_group_path, substring)
            unused_file_count += 1

    # Global statistics
    num_files_in_output = len([name for name in os.listdir(output_dir) if name.endswith('.fa')])
    num_unused_bins = len([name for name in os.listdir(output_dir) if name.startswith('Unused')])
    num_total_bins = num_files_in_output
    num_used_bins = len(all_files) - num_unused_bins
    avg_bins_merged = num_used_bins / num_total_bins if num_total_bins > 0 else 0

    logging.info(f"Total number of bins: {num_total_bins}")
    logging.info(f"Number of used bins: {num_used_bins}")
    logging.info(f"Number of unused bins: {num_unused_bins}")
    logging.info(f"Average number of bins merged: {avg_bins_merged}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Script to merge bins with dRep.")
    parser.add_argument("wd", type=str, help="Path to the working directory")
    parser.add_argument("bin_path", type=str, help="Path to the directory where the bins are stored")
    parser.add_argument("-o", "--output_dir", type=str, default=None, help="Path to the output directory (default: working directory)")
    parser.add_argument("-t", "--threshold", type=float, default=0.95, help="Threshold for merging bins (default: 0.95)")

    args = parser.parse_args()

    if args.output_dir is None:
        args.output_dir = args.wd

    main(args.wd, args.bin_path, args.output_dir, args.threshold)
    

###Part to add some statistics, need to modify manualy directory to be used in other case


# Repertory
directory = '/home/clerempuy/BinStat/dRep/GroupBin/'


data = []

# Find .fa file
for filename in os.listdir(directory):
    if filename.endswith('.fa'):
        cluster_name = filename
        contig_name = ""
        contig_sequence = []
        # open and read the file
        with open(os.path.join(directory, filename), 'r') as file:
            for line in file:
                if line.startswith('>'):  # Line with the name of the contigs
                    if contig_name:  # Add contigs name to list
                        contig_length = sum(len(seq) for seq in contig_sequence)
                        data.append({
                            'Cluster': cluster_name,
                            'Lake name': lake_name,
                            'Num Bin': bin_number,
                            'Name': contig_name,
                            'Length of contigs': contig_length})
                    # Start new contigs name
                    contig_name = line.strip()
                    lake_name = contig_name.split('_')[1]  # the 4 letter after "Bin_"
                    bin_number = contig_name.split('_')[2]  # num of the bin
                    contig_sequence = []
                else:
                    contig_sequence.append(line.strip())  # Ad the sequence
            # Add the last contigs
            if contig_name:
                contig_length = sum(len(seq) for seq in contig_sequence)
                data.append({
                    'Cluster': cluster_name,
                    'Lake name': lake_name,
                    'Num Bin': bin_number,
                    'Name': contig_name,
                    'Length of contigs': contig_length})

# Create dataframe
df = pd.DataFrame(data)
print(df)
output_file = '/home/clerempuy/BinStat/dRep/GroupBin/contigs_summary.csv'
df.to_csv(output_file, index=False)


def calculate_n50(lengths):
    sorted_lengths = sorted(lengths, reverse=True)
    total_length = sum(sorted_lengths)
    cumsum = np.cumsum(sorted_lengths)
    n50 = sorted_lengths[np.where(cumsum >= total_length / 2)[0][0]]
    return n50

# Group by 'Cluster' and 'Lake name' and calculate N50 for each group
n50_scores = df.groupby(['Cluster'])['Length of contigs'].apply(calculate_n50).reset_index()

# Renamme column
n50_scores.rename(columns={'Length of contigs': 'N50 Score'}, inplace=True)
n50_scores['Type'] = n50_scores['Cluster'].apply(lambda x: 'Group' if x.startswith('Group') else 'Unused')

# Visualiser avec un boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Type', y='N50 Score', data=n50_scores, palette="Set2")
plt.title('Boxplot of N50 Scores for Group and Unused Clusters')
plt.xlabel('Cluster Type')
plt.ylabel('N50 Score')
plt.show()

n50_scores = df.groupby(['Cluster'])['Length of contigs'].apply(calculate_n50).reset_index()
n50_scores.rename(columns={'Length of contigs': 'N50 Score'}, inplace=True)

# sort for take only N50 > 10 000
filtered_clusters = n50_scores[n50_scores['N50 Score'] > 10000]
sorted_clusters = filtered_clusters.sort_values(by='N50 Score', ascending=False)

# Creat 2 DataFrames for 'Group' and 'Unused'
group_clusters = sorted_clusters[sorted_clusters['Cluster'].str.startswith('Group')]
unused_clusters = sorted_clusters[sorted_clusters['Cluster'].str.startswith('Unused')]
print("Table:")
print(sorted_clusters)
print("Table of Group Clusters:")
print(group_clusters)
print("Table of Unused Clusters:")
print(unused_clusters)


"""
df_200 = df.head(1000)


# Grouper par 'Cluster' et 'Lake name' et calculer le N50 pour chaque groupe
n50_scores = df_200.groupby(['Cluster', 'Lake name'])['Length of contigs'].apply(calculate_n50).reset_index()

# Renommer la colonne pour plus de clart�
n50_scores.rename(columns={'Length of contigs': 'N50 Score'}, inplace=True)

# Reshaper le dataframe pour qu'il soit dans un format pour une heatmap
heatmap_data = n50_scores.pivot(index='Cluster', columns='Lake name', values='N50 Score')

# Remplir les NaN avec 0 (ou une autre valeur de votre choix)
heatmap_data = heatmap_data.fillna(0)

# Visualiser avec une heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap="RdYlGn_r", annot=False)  # Utiliser une palette rouge-vert invers�e
plt.title('Heatmap of N50 Scores by Cluster and Lake')
plt.show()

"""
