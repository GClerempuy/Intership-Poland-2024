# Répertoire source et cible
SOURCE_DIR=/home/clerempuy/Dowload/*

# Boucle sur chaque fichier .fasta dans le répertoire source
for dir in $SOURCE_DIR; do
  echo "$dir"
  quast.py --fast $dir/*.fasta -o $dir/
done

echo "Traitement terminé."