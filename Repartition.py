import os
import glob
from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np

def get_contig_lengths(file_path):
    """Extrait les longueurs des contigs d'un fichier fasta."""
    contig_lengths = []
    with open(file_path, "r") as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            contig_lengths.append(len(record.seq))
    return contig_lengths

def plot_histogram(data, output_file="contig_length_distribution.png"):
    """Trace un histogramme de la répartition des longueurs des contigs avec une limite sur l'axe Y."""
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(data, bins=50, color='red', edgecolor='black', breaks=50)
    # Limite l'axe Y à 100 000
    plt.ylim(0, 2000)
    plt.xlim(0, 150000)
    # Vérifie si une colonne dépasse la limite de 100 000 et ajoute une annotation
    for i, count in enumerate(n):
        if count > 2000:
            plt.text(bins[i] + (bins[i+1] - bins[i]) / 2, 2000, '2000 +', 
                     ha='center', va='bottom', color='red', fontsize=10, fontweight='bold')
    plt.title('Distribution des longueurs des contigs')
    plt.xlabel('Longueur des contigs (pb)')
    plt.ylabel('Fréquence')
    plt.grid(True)
    plt.savefig(output_file)
    plt.show()

def main(directory):
    """Cherche les fichiers .fa ou .fasta dans le répertoire et les sous-répertoires, puis trace un histogramme."""
    contig_lengths = []
    # Recherche des fichiers .fa ou .fasta dans le répertoire et les sous-répertoires
    fasta_files = glob.glob(os.path.join(directory, '**', '*.fa'), recursive=True) + \
                  glob.glob(os.path.join(directory, '**', '*.fasta'), recursive=True)
    # Extraction des longueurs des contigs pour chaque fichier
    for fasta_file in fasta_files:
        contig_lengths += get_contig_lengths(fasta_file)
    if contig_lengths:
        # Trace l'histogramme
        plot_histogram(contig_lengths)
    else:
        print("Aucun contig trouvé dans les fichiers .fa ou .fasta du répertoire donné.")

if __name__ == "__main__":
    # Remplacez 'votre_repertoire' par le chemin de votre répertoire contenant les fichiers fasta
    directory = "/home/clerempuy/Dowload/"
    main(directory)













import os
import glob
from Bio import SeqIO
import matplotlib.pyplot as plt

def get_contig_lengths(file_path):
    """Extrait les longueurs des contigs d'un fichier fasta."""
    contig_lengths = []
    with open(file_path, "r") as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            contig_lengths.append(len(record.seq))
    return contig_lengths

def plot_histogram(data, output_file="contig_length_distribution.png"):
    """Trace un histogramme de la répartition des longueurs des contigs avec une limite sur l'axe Y."""
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(data, bins=50, color='green', edgecolor='black')
    # Limite l'axe Y à 100 000
    plt.ylim(0, 2000)
    plt.xlim(0, 150000)
    # Vérifie si une colonne dépasse la limite de 100 000 et ajoute une annotation
    for i, count in enumerate(n):
        if count > 2000:
            plt.text(bins[i] + (bins[i+1] - bins[i]) / 2, 2000, '2000 +', 
                     ha='center', va='bottom', color='red', fontsize=10, fontweight='bold')
    plt.title('Distribution des longueurs des contigs')
    plt.xlabel('Longueur des contigs (pb)')
    plt.ylabel('Fréquence')
    plt.grid(True)
    plt.savefig(output_file)
    plt.show()

def main(directory):
    """Cherche les fichiers *PlastidG.fasta dans le répertoire et les sous-répertoires, puis trace un histogramme."""
    contig_lengths = []
    # Recherche des fichiers *PlastidG.fasta dans le répertoire et les sous-répertoires
    fasta_files = glob.glob(os.path.join(directory, '**', '*PlastidG.fasta'), recursive=True)
    # Extraction des longueurs des contigs pour chaque fichier
    for fasta_file in fasta_files:
        contig_lengths += get_contig_lengths(fasta_file)
    if contig_lengths:
        # Trace l'histogramme
        plot_histogram(contig_lengths)
    else:
        print("Aucun contig trouvé dans les fichiers *PlastidG.fasta du répertoire donné.")

if __name__ == "__main__":
    # Remplacez 'votre_repertoire' par le chemin de votre répertoire contenant les fichiers fasta
    directory = "/home/clerempuy/Genius/"
    main(directory)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import os
import glob
from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np

def get_contig_lengths(file_path):
    """Extrait les longueurs des contigs d'un fichier fasta."""
    contig_lengths = []
    with open(file_path, "r") as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            contig_lengths.append(len(record.seq))
    return contig_lengths

def compute_histogram(data, bins):
    """Calcule l'histogramme pour les données données avec les bins spécifiés."""
    n, _ = np.histogram(data, bins=bins)
    return n

def plot_superposed_histogram(data1, data2, bins, output_file="superposed_histogram.png"):
    """Trace un histogramme superposé pour montrer les parties communes et uniques."""
    hist1 = compute_histogram(data1, bins)
    hist2 = compute_histogram(data2, bins)
    common = np.minimum(hist1, hist2)
    unique1 = hist1 - common
    unique2 = hist2 - common
    plt.figure(figsize=(10, 6))
    plt.bar(bins[:-1], common, width=(bins[1] - bins[0]), color='lightblue', label='Commun', edgecolor='black')
    plt.bar(bins[:-1], unique1, width=(bins[1] - bins[0]), color='red', label='Unique au premier', edgecolor='black', bottom=common)
    plt.bar(bins[:-1], unique2, width=(bins[1] - bins[0]), color='green', label='Unique au deuxième', edgecolor='black', bottom=common+unique1)
    plt.ylim(0, 2000)
    plt.xlim(0, 150000)
    plt.title('Histogramme superposé des longueurs des contigs')
    plt.xlabel('Longueur des contigs (pb)')
    plt.ylabel('Fréquence')
    plt.legend()
    plt.grid(True)
    plt.savefig(output_file)
    plt.show()

def main(directory1, directory2, bins):
    """Extrait les longueurs des contigs des deux répertoires et trace un histogramme superposé."""
    contig_lengths1 = []
    contig_lengths2 = []
    # Recherche des fichiers dans les deux répertoires
    fasta_files1 = glob.glob(os.path.join(directory1, '**', '*.fa'), recursive=True) + \
                   glob.glob(os.path.join(directory1, '**', '*.fasta'), recursive=True)
    fasta_files2 = glob.glob(os.path.join(directory2, '**', '*PlastidG.fasta'), recursive=True)
    # Extraction des longueurs des contigs pour chaque fichier
    for fasta_file in fasta_files1:
        contig_lengths1 += get_contig_lengths(fasta_file)
    for fasta_file in fasta_files2:
        contig_lengths2 += get_contig_lengths(fasta_file)
    # Trace l'histogramme superposé
    if contig_lengths1 and contig_lengths2:
        plot_superposed_histogram(contig_lengths1, contig_lengths2, bins)
    else:
        print("Aucun contig trouvé dans les fichiers des répertoires donnés.")

if __name__ == "__main__":
    directory1 = "/home/clerempuy/Dowload/"
    directory2 = "/home/clerempuy/Genius/"
    # Définir les bins communs
    bins = np.linspace(0, 150000, 51)
    main(directory1, directory2, bins)

