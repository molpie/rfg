
# RFG (Random File Generator)

Questo script Python genera file con contenuti casuali a partire da una lista di file presenti in una directory. Il programma elenca tutti i file nella directory, crea un file CSV contenente i nomi dei file e le loro dimensioni, e successivamente genera file con contenuti casuali con le stesse dimensioni e nomi modificati.

## Funzionalità

1. **Elenco dei File e Dimensioni:**

   - Elenca tutti i file presenti in una directory specificata e ottiene le dimensioni di ciascun file.
   - Salva queste informazioni in un file CSV.
2. **Generazione di File Casuali:**

   - Legge il file CSV per ottenere nomi e dimensioni dei file.
   - Genera nuovi file con contenuti casuali della stessa dimensione specificata nel CSV.
   - I nomi dei nuovi file generati sono preceduti dalla lettera "F" per indicare che si tratta di file "fake".

## Utilizzo

1. **Esecuzione dello Script:**

   - Eseguire il programma e inserire il percorso della directory di cui si vogliono elencare i file. Se si lascia il campo vuoto, il programma utilizzerà la directory corrente.
2. **Output:**

   - Un file CSV contenente i nomi e le dimensioni dei file trovati nella directory specificata.
   - Una nuova directory (se non esiste) con file generati casualmente, dove il nome di ogni file è preceduto da "F".

### Esempio di Esecuzione

Eseguire lo script e fornire il percorso della directory:

Inserisci il percorso della directory (lascia vuoto per usare la directory corrente): /percorso/della/directory

Se non viene fornito alcun percorso, verrà utilizzata la directory corrente.

## Requisiti

- Python 3.x
- Moduli: `os`, `csv`, `random`

## Note

- Assicurarsi di avere i permessi necessari per creare file e directory.
- Verificare che ci sia spazio sufficiente sul disco per i file generati.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedere il file `LICENSE` per i dettagli.
