import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

df = pd.read_csv("/home/clerempuy/BinStat/dRep/GroupBin/contigs_summary.csv", sep=",")
def calculate_n50(lengths): #Cacul N50
    sorted_lengths = sorted(lengths, reverse=True)
    total_length = sum(sorted_lengths)
    cumsum = np.cumsum(sorted_lengths)
    n50 = sorted_lengths[np.where(cumsum >= total_length / 2)[0][0]]
    return n50
# Calcul N50 per cluster
n50_scores = df.groupby(['Cluster'])['Length of contigs'].apply(calculate_n50).reset_index()
n50_scores.rename(columns={'Length of contigs': 'N50 Score'}, inplace=True)
# take N50 > 10 000
filtered_clusters = n50_scores[n50_scores['N50 Score'] > 100000]
print(filtered_clusters)



####### Comparaison of cluster size (total length per cluster)   ###########
# Cacul total length per cluster
lake_lengths = df.groupby('Lake name')['Length of contigs'].sum().reset_index()
lake_lengths = lake_lengths.sort_values(by='Length of contigs', ascending=False)

# Pr�parer les donn�es pour le diagramme camembert
labels = lake_lengths['Lake name']
sizes = lake_lengths['Length of contigs']
total_size = sizes.sum()
percentages = sizes / total_size * 100
num_colors = len(labels)
colors = plt.get_cmap('tab20', num_colors)

# Create the diagram camembert
plt.figure(figsize=(12, 10))
plt.pie(sizes, labels=[f'{label}: {percent:.1f}%' for label, percent in zip(labels, percentages)],
        colors=colors(range(num_colors)), startangle=140, wedgeprops=dict(width=0.4), 
        pctdistance=0.85, labeldistance=None)  # Retirer les labels internes
plt.legend(
    handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors(i), markersize=10, linestyle='') 
             for i in range(num_colors)],
    labels=[f'{label}: {percent:.1f}%' for label, percent in zip(labels, percentages)],
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    title='Lakes',
    title_fontsize='13',
    fontsize='11',
    ncol=3,  # Number of column for the legend
    frameon=False
)
plt.title('Distribution of Contig Lengths by Lake in All Clusters')
plt.axis('equal') 
plt.show()





# take N50 > 100 000
top_n50_clusters = n50_scores[n50_scores['N50 Score'] > 100000]
top_clusters = top_n50_clusters['Cluster']
filtered_df = df[df['Cluster'].isin(top_clusters)]

# Create table of presence/absence of lakes for each cluster
filtered_df['Presence'] = 1
pivot_table = filtered_df.pivot_table(index='Lake name', columns='Cluster', values='Presence', fill_value=0, aggfunc='max')
custom_cmap = sns.color_palette(["#f27f7fff", "#489b5bff"])
sns.set(font_scale=1.2)

# Create the HeatMap
plt.figure(figsize=(14, 10))
sns.heatmap(pivot_table, cmap=custom_cmap, cbar=False, linewidths=0.5)

plt.title('Heatmap of lakes for clusters with N50 > 100 000', fontsize=18)
plt.xlabel('Cluster', fontsize=15)
plt.ylabel('Lake Name', fontsize=15)
plt.xticks(rotation=90, fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout()
plt.show()


