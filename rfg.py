import os
import csv
import random

def list_files_in_directory(directory, output_csv):
    # Elenca tutti i file nella directory specificata
    files = os.listdir(directory)
    
    # Filtra solo i file (esclude le cartelle)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    
    # Ottieni le dimensioni dei file e scrivili in un CSV
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Filename', 'Size'])
        
        for filename in files:
            filepath = os.path.join(directory, filename)
            size = os.path.getsize(filepath)
            writer.writerow([filename, size])
            print(f"File: {filename}, Size: {size} bytes")

def create_random_files_from_csv(csv_filename):
    # Estrarre il nome base del file CSV senza l'estensione
    base_dir = os.path.splitext(csv_filename)[0]
    
    # Creare la directory se non esiste
    os.makedirs(base_dir, exist_ok=True)
    
    with open(csv_filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Salta l'intestazione
        for row in reader:
            filename, size = row
            size = int(size)  # Convertire la dimensione del file in intero
            create_random_file(base_dir, filename, size)

def create_random_file(base_dir, filename, size):
    # Genera contenuto casuale
    content = os.urandom(size)
    
    # Anteponi "F" al nome del file
    new_filename = "F" + filename
    
    # Costruisce il percorso completo del file
    file_path = os.path.join(base_dir, new_filename)
    
    with open(file_path, 'wb') as file:
        file.write(content)
    print(f"Creato file: {file_path}, Dimensione: {size} byte")

# Funzione principale
def process_directory(directory='.'):
    # Usa la directory corrente se non viene specificata una directory
    if not directory:
        directory = os.getcwd()
    
    output_csv = os.path.join(directory, f"{os.path.basename(directory)}_file_list.csv")
    list_files_in_directory(directory, output_csv)
    create_random_files_from_csv(output_csv)

# Esempio di utilizzo
directory = input("Inserisci il percorso della directory (lascia vuoto per usare la directory corrente): ").strip()
process_directory(directory)
