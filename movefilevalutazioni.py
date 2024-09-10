import os
import shutil
import pandas as pd

# Leggi il file CSV
def crea_struttura_e_sposta_documenti(csv_path, base_dir):
    # Carica il CSV in un DataFrame pandas
    df = pd.read_csv(csv_path)

    # Loop su ogni riga del CSV
    for index, row in df.iterrows():
        # Estrai i valori delle colonne necessarie
        dataquarter = row['dataquarter']
        ufficio = row['ufficio']
        tipocontribuzione = row['tipocontribuzione']
        nomedocumento = row['nomedocumento']
        
        # La colonna 'tipologiadocumento' potrebbe non essere sempre presente
        tipologiadocumento = row.get('tipologiadocumento', None)
        
        # Crea il percorso della directory di destinazione
        if tipologiadocumento:
            dest_dir = os.path.join(base_dir, dataquarter, ufficio, tipocontribuzione, tipologiadocumento)
        else:
            dest_dir = os.path.join(base_dir, dataquarter, ufficio, tipocontribuzione)
        
        # Crea la directory se non esiste
        os.makedirs(dest_dir, exist_ok=True)
        
        # Percorso del file sorgente
        src_file = os.path.join(base_dir, dataquarter, nomedocumento)
        
        # Percorso di destinazione del file
        dest_file = os.path.join(dest_dir, nomedocumento)
        
        # Sposta il file nella directory di destinazione
        if os.path.exists(src_file):
            shutil.move(src_file, dest_file)
            print(f'Spostato {nomedocumento} in {dest_dir}')
        else:
            print(f'File {src_file} non trovato')

# Esegui la funzione con il path del CSV e la directory base
csv_path = 'ALL.csv'
base_dir = '/C:/Users/molin195/Downloads/Test_BPM/1.SVIL/'
crea_struttura_e_sposta_documenti(csv_path, base_dir)
