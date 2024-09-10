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
        
        # # La colonna 'tipologiadocumento' potrebbe non essere presente o avere un valore NaN
        # tipologiadocumento = row.get('tipologiadocumento', None)
        
        # # Controlla se tipologiadocumento è una stringa, altrimenti imposta a None
        # if isinstance(tipologiadocumento, str):
        #     tipologiadocumento = tipologiadocumento.strip()
        # else:
        #     tipologiadocumento = None
        
        # # Crea il percorso della directory di destinazione
        # if tipologiadocumento:
        #     dest_dir = os.path.join(base_dir, "new", dataquarter, ufficio, tipocontribuzione, tipologiadocumento)
        # else:
        #     dest_dir = os.path.join(base_dir, "new", dataquarter, ufficio, tipocontribuzione)
        #
        # Versione semplificata
        dest_dir = os.path.join(base_dir, "new", dataquarter, ufficio, tipocontribuzione)

        # Crea la directory se non esiste
        os.makedirs(dest_dir, exist_ok=True)
        
        # Percorso del file sorgente
        src_file = os.path.join(base_dir, dataquarter, nomedocumento)
        
        # Percorso di destinazione del file
        dest_file = os.path.join(dest_dir, nomedocumento)
        
        # Sposta il file nella directory di destinazione
        if os.path.exists(src_file):
            shutil.copy(src_file, dest_file)
            print(f'Copiato {nomedocumento} in {dest_dir}')
        else:
            print(f'File {src_file} non trovato')

# Esegui la funzione con il path del CSV e la directory base
csv_path = 'ALL.csv'
base_dir = 'C:/SW/hashsum/downloads/Test/'
crea_struttura_e_sposta_documenti(csv_path, base_dir)
