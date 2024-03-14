import os

os.system('python -m spotdl --download-ffmpeg')

if not os.path.exists('downloads'):
    os.makedirs('downloads')

with open('links.txt', 'r') as file:
    os.chdir('downloads')
    for line in file:
        os.system(f'python -m spotdl {line}')