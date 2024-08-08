import os
import csv
import random
import pandas as pd

def get_document_details(csv_file, document_name):
    """
    Ottiene i dettagli del documento (ufficio e tipocontribuzione) dal file CSV.
    """
    df = pd.read_csv(csv_file)
    document_row = df[df['nomedocumento'] == document_name]
    
    if document_row.empty:
        raise ValueError(f"Documento {document_name} non trovato nel file CSV.")
    
    ufficio = document_row.iloc[0]['ufficio']
    tipocontribuzione = document_row.iloc[0]['tipocontribuzione']
    
    return ufficio, tipocontribuzione

def create_random_files_from_csv(files_csv, details_csv, dest_directory):
    """
    Crea file casuali con dimensioni specificate in base alle informazioni fornite in un file CSV
    e salva i file nelle sottodirectory 'ufficio' e 'tipocontribuzione'.
    """
    try:
        with open(files_csv, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Salta l'intestazione
            
            for row in reader:
                filename, size = row
                size = int(size)
                
                # Ottieni ufficio e tipocontribuzione dal CSV dei dettagli
                ufficio, tipocontribuzione = get_document_details(details_csv, filename)
                
                # Creare la struttura delle directory
                base_dir = os.path.join(dest_directory, ufficio, tipocontribuzione)
                os.makedirs(base_dir, exist_ok=True)
                
                # Crea il file casuale
                create_random_file(base_dir, filename, size)
    except Exception as e:
        print(f"Errore durante la creazione dei file dalla CSV {files_csv}: {e}")

def create_random_file(base_dir, filename, size):
    """
    Crea un file con contenuto casuale e dimensione specificata.
    """
    content = os.urandom(size)
    new_filename = "F" + filename
    file_path = os.path.join(base_dir, new_filename)
    
    try:
        with open(file_path, 'wb') as file:
            file.write(content)
        print(f"Creato file: {file_path}, Dimensione: {size} byte")
    except Exception as e:
        print(f"Errore durante la creazione del file {file_path}: {e}")

def process_directory(files_csv, details_csv, output_directory=None):
    """
    Processa un file CSV contenente i nomi e le dimensioni dei file e crea file casuali
    in base alle dimensioni elencate, utilizzando i dettagli del CSV per determinare le sottodirectory.
    """
    if not output_directory:
        output_directory = os.getcwd()
    
    create_random_files_from_csv(files_csv, details_csv, output_directory)

# Esempio di utilizzo
files_csv = input("Inserisci il percorso del file CSV con l'elenco dei file e delle dimensioni: ").strip()
details_csv = input("Inserisci il percorso del file CSV con i dettagli (ufficio e tipocontribuzione): ").strip()
output_directory = input("Inserisci il percorso della directory di destinazione (lascia vuoto per usare la directory corrente): ").strip()
process_directory(files_csv, details_csv, output_directory)
