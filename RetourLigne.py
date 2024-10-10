# -*- coding: utf-8 -*-


import argparse

def main(input_file, output_file):
    # Ouvrir le fichier en lecture
    with open(input_file, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()

    # Remplacer chaque '>' par '\n>'
    contenu_modifie = contenu.replace('>', '\n>')

    # Écrire le contenu modifié dans un nouveau fichier ou écraser l'ancien fichier
    with open(output_file, 'w', encoding='utf-8') as fichier:
        fichier.write(contenu_modifie)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script pour modifier un fichier en remplacant '>' par '\n>'")
    parser.add_argument("-i", "--input", help="Chemin vers le fichier d entree", required=True)
    parser.add_argument("-o", "--output", help="Chemin vers le fichier de sortie", required=True)
    args = parser.parse_args()

    main(args.input, args.output)
