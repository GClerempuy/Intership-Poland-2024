# -*- coding: utf-8 -*-
import pandas as pd
from graphviz import Digraph

# Define color
colors = {
    'vert_clair': '#90EE90',
    'bleu_medium': '#6495ED',
    'rouge_bordeau_sombre': '#800000',
    'orange_leger': '#FFD700',
    'Autre': '#000000'
}

# Load file
df = pd.read_csv("Diagramme.csv", sep=";", header=0)

# Begin graph
dot = Digraph()
dot.attr(dpi='1000')  #Image quality

# Add nodes
nodes = set(df['Input'].tolist() + df['Output'].tolist() + df['Script'].tolist())

# add nodes and find color
for node in nodes:
    if node in df['Input'].tolist() + df['Output'].tolist():
        
        color = df.loc[(df['Input'] == node) | (df['Output'] == node), 'Color'].iloc[0]
        dot.node(node, shape='box', color=color, penwidth='2.0', fontsize='16')  # square form for files
    else:
        color = df.loc[df['Script'] == node, 'Color'].iloc[0]
        dot.node(node, color=color, penwidth='2.0', fontsize='16')  # circle form for script

added_edges = set()

# add link
for _, row in df.iterrows():
    input_value = str(row['Input'])
    script = row['Script']
    output_value = str(row['Output']) 
    
    if input_value and script:
        edge = (input_value, script)
        if edge not in added_edges:  
            dot.edge(input_value, script)
            added_edges.add(edge)
    if script and output_value:
        edge = (script, output_value)
        if edge not in added_edges: 
            dot.edge(script, output_value)
            added_edges.add(edge)

# Save all
dot.render('diagram', format='pdf', view=False)
dot.render('diagram', format='png', view=False)




###Same than before but with the other file

df = pd.read_csv("DiagrammeSimple.csv", sep=";", header=0)
dot = Digraph()
dot.attr(dpi='600', rankdir='TB', splines='polyline')  
color_dict = {
    'Fasta_files_with_contigs': '#6495ED',
    'Test_Part': '#6495ED',
    'Statistique_And_Other_Tests': '#6495ED',
    'Tiara.sh': '#006400',
    'Plastid_And_Mitochondrion_Contigs': '#006400',
    'Quast.sh': '#800000',
    'quast_stat_of_all_contigs': '#800000',
    'MakeTable.sh': '#800000',
    'Resume_Table_of_data_from_contigs': '#800000',
    'Group_by_name': '#000000',
    'Plastid_And_Mitochondrion_Contigs_grouped_by_name': '#000000',
    'Geneious.sh': '#FFD700',
    'Plastid_and_mitochondrion_contigs_reassembled_and_grouped_by_name.': '#FFD700',
    'quast_stat_of_Plastid_and_Mitochondrion_contigs': '#800000',
    'bbtools.sh': '#800000',
    'bbtools_stat_of_Plastid_and_Mitochondrion_contigs_after_Geneious': '#800000'
}
first_steps = set(df['Input']) - set(df['Output'])
nodes = set(df['Input'].tolist() + df['Output'].tolist() + df['Script'].tolist())
with dot.subgraph() as s:
    s.attr(rank='same')
    for node in first_steps:
        color = color_dict.get(node, '#000000')
        s.node(node, shape='box', color=color, penwidth='2.0', fontsize='25')

for node in nodes - first_steps:
    if node in df['Input'].tolist() + df['Output'].tolist():
        color = color_dict.get(node, '#000000')
        dot.node(node, shape='box', color=color, penwidth='2.0', fontsize='25')
    else:
        color = color_dict.get(node, '#000000')
        dot.node(node, color=color, penwidth='2.0', fontsize='25')

def edge_length(input_value, output_value):
    input_index = df[df['Input'] == input_value].index.tolist()
    output_index = df[df['Output'] == output_value].index.tolist()
    if input_index and output_index:
        return abs(output_index[0] - input_index[0])
    return 0
s
added_edges = set()

for _, row in df.iterrows():
    input_value = row['Input']
    script = row['Script']
    output_value = row['Output']
    
    if input_value and script:
        edge = (input_value, script)
        if edge not in added_edges: 
            style = 'solid'
            if edge_length(input_value, script) > 1:
                style = 'dashed'
            dot.edge(input_value, script, style=style)
            added_edges.add(edge)
    if script and output_value:
        edge = (script, output_value)
        if edge not in added_edges: 
            style = 'solid'
            if edge_length(script, output_value) > 1:
                style = 'dashed'
            dot.edge(script, output_value, style=style)
            added_edges.add(edge)

dot.render('diagramSimple', format='pdf', view=False)
dot.render('diagramSimple', format='png', view=False)
