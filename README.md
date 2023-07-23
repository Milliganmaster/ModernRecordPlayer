# RFID Music Player - README

This repository contains code for an RFID Music Player that allows you to associate RFID tags with specific songs, playlists, albums, or artists on Spotify. When the RFID tag is scanned using a compatible reader, the associated music will be played through the connected speakers.
Hardware Requirements

## To run this RFID Music Player, you will need the following hardware components:

    Raspberry Pi (with Raspbian OS or compatible)
    MFRC522 RFID Reader
    RFID Tags or Cards (compatible with MFRC522)
    Speakers (connected to the Raspberry Pi)
    Internet connectivity for Spotify playback

## Setup Instructions

    Install Dependencies: Before running the code, ensure that you have installed the necessary dependencies. This includes Python, Spotipy (a Python library for Spotify), and RPi.GPIO (for GPIO control on the Raspberry Pi). You can install Spotipy using pip:

    bash

    pip install spotipy

    Spotify Account and Credentials: Create a Spotify developer account and obtain the CLIENT_ID and CLIENT_SECRET required for authentication. These credentials are used to interact with the Spotify API. Replace the placeholders CLIENT_ID and CLIENT_SECRET in the code with your actual credentials.

    Associate RFID Tags: Run the read.py script to find the ID numbers of your RFID tags/cards. When you scan an RFID tag, the associated ID number will be displayed in the console. Note down these ID numbers for each RFID tag you want to use.

    Customize Music Association: Open the player.py script and customize the associations between RFID tags and Spotify music. You can associate RFID tags with specific songs, playlists, albums, or artists by adding more elif conditions in the code. Replace the placeholder IDs in the if conditions with the RFID tag ID numbers you noted down earlier. Add the Spotify URIs for the songs, playlists, albums, or artists you want to play when the corresponding RFID tags are scanned.

    Run the RFID Music Player: Once you have set up the associations, run the player.py script on your Raspberry Pi. The program will continuously wait for an RFID tag to be scanned. When a known tag is detected, the associated music will be played on the connected speakers.

    Enjoy Your Music: Touch an RFID tag to the RFID reader, and the music associated with that tag will start playing through the connected speakers.

## Notes and Tips

    Make sure your Raspberry Pi is connected to the internet so that Spotify can stream the music.
    Ensure that the RFID tags/cards are compatible with the MFRC522 reader used in the project.
    The sleep time (sleep(2)) after starting playback or adding to the queue is added to allow the music player some time to process the request. You can adjust this value as needed.
    Feel free to extend the associations to include more RFID tags and corresponding music choices.
    Handle exceptions gracefully. If there are any errors during execution, the code will skip them and continue to wait for the next RFID tag scan.
