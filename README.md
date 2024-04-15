# Spotify Playlist Downloader

## Description

This simple Python script automates downloading songs from Spotify playlists using the `spotdl` library.

## Prerequisites

-   **Python 3:** Download and install the latest Python version from [www.python.org/downloads/](https://www.python.org/downloads/)
-   **spotdl:** [github.com/spotDL/spotify-downloader](https://github.com/spotDL/spotify-downloader)

## Setup

1. **Install the `spotdl` library:**

    ```bash
    pip install spotdl
    ```

2. **Input links to the 'links.txt' file:** Place the links to Spotify songs/albums/playlists in this file, one link per line.

## Usage

Run the script from your terminal:

```bash
python main.py
```

If prompted

```bash
FFmpeg is already installed. Do you want to overwrite it? (y/N):
```

1. Type `y` and press `Enter` to download the latest version of FFmpeg.

2. Type `N` and press `Enter` to use the existing FFmpeg installation.

    If you get the following error:

    ```bash
    OSError: [WinError 193] %1 is not a valid Win32 application
    ```

    Go back to option 1 and overwrite the existing FFmpeg installation.

## Explanation

The script does the following:

-   **Imports the `os` module:** Used for interacting with the operating system (changing directories, running commands).
-   **Downloads ffmpeg (if not present):** Ensures that `spotdl` has its necessary dependency.
-   **Reads the `links.txt` file:** Iterates through each Spotify playlist link.
-   **Downloads songs using `spotdl`:** Uses the `spotdl` library to download the tracks from each playlist.
