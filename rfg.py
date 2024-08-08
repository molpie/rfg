import os
import csv
import random
import pandas as pd
import string
import zipfile
from io import BytesIO
from openpyxl import Workbook

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
    file_extension = os.path.splitext(filename)[1].lower()
    new_filename = "F" + filename
    file_path = os.path.join(base_dir, new_filename)
    
    try:
        if file_extension in ['.txt', '.csv']:
            content = ''.join(random.choices(string.ascii_letters + string.digits, k=size)).encode('utf-8')
        elif file_extension in ['.bin', '.dat', '.rar']:
            content = generate_dummy_rar(size)
        elif file_extension == '.pdf':
            content = generate_dummy_pdf(size)
        elif file_extension in ['.zip']:
            content = generate_dummy_zip(size)
        elif file_extension in ['.xlsx', '.xlsm']:
            generate_dummy_excel(file_extension, file_path, size)
            return  # Il file Excel è già stato scritto, quindi esci dalla funzione
        else:
            content = os.urandom(size)  # default to random binary content for unknown extensions
        
        with open(file_path, 'wb') as file:
            file.write(content)
        print(f"Creato file: {file_path}, Dimensione: {size} byte")
    except Exception as e:
        print(f"Errore durante la creazione del file {file_path}: {e}")

def generate_dummy_pdf(size):
    """
    Genera un contenuto dummy per un file PDF di dimensioni approssimative specificate.
    """
    header = b'%PDF-1.4\n%PDF\n'
    body = b'1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n'
    body += b'2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n'
    body += b'3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>\nendobj\n'
    body += b'4 0 obj\n<< /Length 44 >>\nstream\nBT /F1 24 Tf 100 700 Td (Hello, PDF!) Tj ET\nendstream\nendobj\n'
    body += b'5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n'
    body += b'xref\n0 6\n0000000000 65535 f \n0000000010 00000 n \n0000000079 00000 n \n0000000178 00000 n \n'
    body += b'0000000375 00000 n \n0000000450 00000 n \ntrailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n545\n%%EOF'
    
    # Se il body è più grande della dimensione desiderata, taglialo
    if len(header) + len(body) > size:
        return header + body[:size - len(header)]
    # Altrimenti, riempi con contenuto random
    else:
        filler = os.urandom(size - len(header) - len(body))
        return header + body + filler

def generate_dummy_zip(size):
    """
    Genera un contenuto dummy per un file ZIP di dimensioni approssimative specificate.
    """
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zf:
        zf.writestr('dummy.txt', 'This is a dummy text file.')
    zip_content = buffer.getvalue()
    
    if len(zip_content) > size:
        return zip_content[:size]
    else:
        return zip_content + os.urandom(size - len(zip_content))

def generate_dummy_rar(size):
    """
    Genera un contenuto dummy per un file RAR di dimensioni approssimative specificate.
    """
    header = b'Rar!\x1A\x07\x00'
    body = b'\x00' * (size - len(header))
    
    if len(header) + len(body) > size:
        return header + body[:size - len(header)]
    else:
        return header + body

def generate_dummy_excel(extension, file_path, size):
    """
    Genera un file Excel dummy con estensione specificata e lo salva nel percorso specificato.
    """
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Hello, Excel!'
    buffer = BytesIO()
    wb.save(buffer)
    
    excel_content = buffer.getvalue()
    
    with open(file_path, 'wb') as f:
        f.write(excel_content)
        # Calcola quanto contenuto casuale aggiungere per raggiungere la dimensione desiderata
        current_size = len(excel_content)
        if current_size < size:
            f.write(os.urandom(size - current_size))
    
    print(f"Creato file Excel: {file_path}, Dimensione: {size} byte")

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
