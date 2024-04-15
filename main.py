import os
import threading

os.system('python -m spotdl --download-ffmpeg')

if not os.path.exists('downloads'):
    os.makedirs('downloads')

def download_song(song_link):
    os.system(f'python -m spotdl {song_link}')

with open('links.txt', 'r') as file:
    os.chdir('downloads')
    threads = []
    for line in file:
        thread = threading.Thread(target=download_song, args=(line,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()