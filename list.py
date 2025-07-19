import os

def genera_lista_files(cartella):
    # Verifica che la cartella esista
    if not os.path.exists(cartella):
        print(f"Errore: la cartella '{cartella}' non esiste.")
        return ""
    
    # Prendi tutti i file nella cartella
    files = os.listdir(cartella)
    if not files:
        print(f"La cartella '{cartella}' è vuota.")
        return ""
    
    print(f"Files trovati nella cartella: {files}")  # Debug
    
    # Filtra i file che seguono il formato "reel_X.mp4" dove X è un numero da 1 a 50
    reel_files = [f for f in files if f.startswith("reel_") and f[5:-4].isdigit()]
    
    if not reel_files:
        print("Nessun file 'reel_X.mp4' trovato.")
        return ""
    
    # Ordina i file numericamente per "reel_X"
    reel_files.sort(key=lambda x: int(x[5:-4]))  # Estrai il numero da "reel_X" per l'ordinamento
    
    # Crea il formato richiesto per ogni file
    risultati = []
    for i, file in enumerate(reel_files):
        # Costruisci il percorso del file usando '/' come separatore
        percorso = f"videos/{file}"
        risultato = f"{{ type: 'video', src: '{percorso}', name: 'video {file}' }}"
        
        # Aggiungi la virgola alla fine di ogni riga, eccetto per l'ultimo file
        if i < len(reel_files) - 1:
            risultato += ","
        
        risultati.append(risultato)
    
    return "\n".join(risultati)

# Definisci il percorso della cartella
cartella_videos = "videos"  # Assicurati che la cartella 'videos' esista nella stessa directory

# Genera la lista ordinata
output = genera_lista_files(cartella_videos)

if output:
    # Stampa l'output (puoi anche salvarlo su un file)
    print(output)

    # Salva l'output su un file .txt
    with open('output.txt', 'w') as f:
        f.write(output)
else:
    print("Nessun risultato da scrivere nel file.")
