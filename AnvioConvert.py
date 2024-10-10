import gzip
import csv
import os

def rename_fasta_headers(input_file, output_file):
    name_mapping = {}
    counter = 1
    with gzip.open(input_file, 'rt') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith(">"):
                new_name = f">c{counter:04d}" #New name
                old_name = line.strip()
                name_mapping[old_name] = new_name
                outfile.write(new_name + "\n") #Write name
                counter += 1
            else:
                outfile.write(line)
    return name_mapping

#Repertory
input_directory = '/home/clerempuy/ForMapping'

#Take all file
for file_name in os.listdir(input_directory):
    if file_name.endswith('.fasta.gz'):
        input_file = os.path.join(input_directory, file_name)
        
        base_name = os.path.basename(input_file)#Take file name
        file_name_without_ext = os.path.splitext(os.path.splitext(base_name)[0])[0]
        #Renamed path
        output_file = os.path.join(input_directory, f"{file_name_without_ext}_renamed.fasta")
        
        # Rename header
        name_mapping = rename_fasta_headers(input_file, output_file)
        
        # Create correspondance name table
        csv_filename = os.path.join(input_directory, f"{file_name_without_ext}.csv")
        
        # Write it
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Old Name", "New Name"])
            for old_name, new_name in name_mapping.items():
                writer.writerow([old_name, new_name])
        
        print(f"Data save in the file : {csv_filename}")
