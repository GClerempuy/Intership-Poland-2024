import csv
import re

# Define the input and output file paths
input_file = 'Test/testbbtools.txt'
output_file = 'Test/testbbtools.csv'

# Initialize lists to store different sections of the data
summary_data = []
scaffold_data = []

with open(input_file, 'r') as infile:
    lines = infile.readlines()

    # Parse the summary data
    for i, line in enumerate(lines):
        if re.match(r'^A\s+C\s+G\s+T\s+N\s+IUPAC\s+Other\s+GC\s+GC_stdev$', line.strip()):
            summary_data = lines[i + 1].strip().split()
            break

    # Parse the scaffold data
    for i, line in enumerate(lines):
        if re.match(r'^Minimum\s+Number\s+Number\s+Total\s+Total\s+Scaffold$', line.strip()):
            scaffold_start_index = i + 2
            break

    scaffold_data = [line.strip().split() for line in lines[scaffold_start_index:]]

# Write the data to a CSV file
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the summary data
    csvwriter.writerow(['A', 'C', 'G', 'T', 'N', 'IUPAC', 'Other', 'GC', 'GC_stdev'])
    csvwriter.writerow(summary_data)
    
    # Write the scaffold data
    csvwriter.writerow(['Minimum Scaffold Length', 'Number of Scaffolds', 'Number of Contigs',
                        'Total Scaffold Length', 'Total Contig Length', 'Scaffold Contig Coverage'])
    csvwriter.writerows(scaffold_data)
