import instaloader
import requests
import os

# Funzione per scaricare i Reels
def download_reels_with_instaloader(profile_name, sessionid):
    # Crea la cartella "videos" se non esiste
    if not os.path.exists("videos"):
        os.makedirs("videos")

    L = instaloader.Instaloader()

    # Aggiungi il cookie di sessione al contesto di Instaloader
    L.context._session.cookies.set('sessionid', sessionid)

    # Scarica il profilo
    profile = instaloader.Profile.from_username(L.context, profile_name)

    # Limita a scaricare tutti i Reels
    count = 0
    for post in profile.get_posts():
        if post.is_video:  # Verifica se il post è un video (Reels)
            video_url = post.video_url  # Ottieni il link del video
            print(f"Reel video URL: {video_url}")

            try:
                # Scarica il video
                video_data = requests.get(video_url, timeout=10).content  # Timeout per evitare blocchi

                # Salva il video nella cartella "videos"
                video_filename = f"videos/reel_{count+1}.mp4"
                with open(video_filename, 'wb') as video_file:
                    video_file.write(video_data)

                print(f"Video {count+1} scaricato con successo: {video_filename}")
                count += 1

            except requests.exceptions.RequestException as e:
                print(f"Errore nel download del video {count+1}: {e}")

# Inserisci il nome dell'account Instagram
profile_name = 'charliepuglisi'

# Inserisci il tuo cookie sessionid qui
sessionid = '60299008160%3A8Lgc0WJs9ZSBE3%3A9%3AAYcM6hWM0YUzod-n1cQg1n_iCZCnDg3sF6bhVQUWVg'

# Avvia il download dei Reels
download_reels_with_instaloader(profile_name, sessionid)
