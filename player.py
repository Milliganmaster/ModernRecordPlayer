#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

CLIENT_ID="b1d9811c8423481db3bf2545c54d9262"
CLIENT_SECRET="d6233f3961b6444faad0c04ff236a9ad"

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            if (id==2275869475):
                
                # Bonzai
                sp.add_to_queue(uri='spotify:track:5CmGNAanGgiB0bvXfFpMeK',device_id=None)
                sleep(2)
                
            elif (id==689856906128):
                
                # Toronto
                sp.start_playback(device_id=None, context_uri='spotify:playlist:6MPBp3ZjbPBvrk0zZs3XMd')
                sleep(2)
            
            elif (id==826741883670):
                
                # Blend
                sp.start_playback(device_id=None, context_uri='spotify:playlist:37i9dQZF1EJDgaiOp7i58p')
                sleep(2)
                
            elif (id==964549936088):
                
                # Ado
                sp.start_playback(device_id=None, context_uri='spotify:artist:6mEQK9m2krja6X1cfsAjfl')
                sleep(2)
                
            elif (id==276700922758):
                
                # 72 Seasons
                sp.start_playback(device_id=None, context_uri='spotify:album:70uejEPPRPSLBrTRdfghP5')
                sleep(2)
                
            elif (id==689772954518):
                
                # Lofi
                sp.start_playback(device_id=None, context_uri='spotify:playlist:1QcsybeUidDJIrPQTHS6dD')
                sleep(2)
                
            elif (id==345286247325):
                
                # Jotaro/naab
                sp.start_playback(device_id=None, context_uri='spotify:playlist:5ubrW0MR8QQd3h0G2pYzzG')
                sleep(2)
                
            elif (id==414660100931):
                
                # American Idiot
                sp.start_playback(device_id=None, context_uri='spotify:album:5dN7F9DV0Qg1XRdIgW8rke')
                sleep(2)
                
            elif (id==4273079119):
                
                # UTA Film Red
                sp.start_playback(device_id=None, context_uri='spotify:album:7Ixqxq13tWhrbnIabk3172')
                sleep(2)
                
            elif (id==828621587356):
                
                # Dance Gavin Dance
                sp.start_playback(device_id=None, context_uri='spotify:artist:6guC9FqvlVboSKTI77NG2k')
                sleep(2)
            
            elif (id==1030921257798):
                
                # Metallica
                sp.start_playback(device_id=None, context_uri='spotify:artist:2ye2Wgw4gimLv2eAKyk1NB')
                sleep(2)
                
            elif (id==828722185089):
                
                # FFDP
                sp.start_playback(device_id=None, context_uri='spotify:artist:5t28BP42x2axFnqOOMg3CM')
                sleep(2)
                
            elif (id==553844212672):
                
                # Amalee
                sp.start_playback(device_id=None, context_uri='spotify:artist:4sf4DrAOkheqktxTyKm7tO')
                sleep(2)
                
            elif (id==622194590718):
                
                # Father Figure 3
                sp.start_playback(device_id=None, context_uri='spotify:album:0vXeeb0BRZOZqkfARsPNA3')
                sleep(2)
                
            elif (id==141074301780):
                
                # Anime NYC 2022
                sp.start_playback(device_id=None, context_uri='spotify:playlist:61DvYy1jU0jJjWBtAGYy18')
                sleep(2)
                
            elif (id==3366847333):
                
                # Anime Playlist
                sp.start_playback(device_id=None, context_uri='spotify:playlist:43z9onpJuM2MBuRAhwooRC')
                sleep(2)
                
            elif (id==827631469535):
                
                # Plastic Beach
                sp.start_playback(device_id=None, context_uri='spotify:album:2dIGnmEIy1WZIcZCFSj6i8')
                sleep(2)
                
            elif (id==965053580287):
                
                # Justice For None
                sp.start_playback(device_id=None, context_uri='spotify:album:38kod5kmO4ZDEetbop1dO2')
                sleep(2)
                
            elif (id==1032700953412):
                
                # Kid A
                sp.start_playback(device_id=None, context_uri='spotify:album:6GjwtEZcfenmOf6l18N7T7')
                sleep(2)
            
            elif (id==208469820287):
                
                # Songs to drive badly to (John)
                sp.start_playback(device_id=None, context_uri='spotify:playlist:7CxVIgJFCyoUEK2VD4tF3t')
                sleep(2)
                
            elif (id==276904084478):
                
                # Backlight
                sp.add_to_queue(uri='spotify:track:3WY0iazRPHOlIq6CdbKLZ6',device_id=None)
                sleep(2)
                
            elif (id==620820169692):
                
                # Crossroads
                sp.start_playback(device_id=None, context_uri='spotify:playlist:6Cv7M7pJkPIqffCUhgaifB')
                sleep(2)
                
            
            elif (id==276920796158):
                
                # Bambi
                sp.add_to_queue(uri='spotify:track:6wQXjA6KWbwPT3ydQCsJ4P',device_id=None)
                sleep(2)
                
            elif (id==964014834515):
                
                # moonwalk
                sp.add_to_queue(uri='spotify:track:0bJQ2EJndGgy6gN63wSHty',device_id=None)
                sleep(2)
                
            elif (id==345237488624):
                
                # Jesus of Serbia
                sp.add_to_queue(uri='spotify:track:58KPPL1AdLHMvR2O2PZejr',device_id=None)
                sleep(2)
                
            elif (id==413621421036):
                
                # Daily Mix
                sp.start_playback(device_id=None, context_uri='spotify:playlist:37i9dQZF1E38NXjlng6C80')
                sleep(2)
                
            elif (id==209005904675):
                
                # Nightmares Made Flesh
                sp.start_playback(device_id=None, context_uri='spotify:album:4qb67R7cFNvFi5jrpRIlkx')
                sleep(2)
                
            elif (id==71130678052):
                
                # Bloodbath
                sp.start_playback(device_id=None, context_uri='spotify:artist:7eYmDBinb760MUIfoRdlGQ')
                sleep(2)
                
            elif (id==895479186197):
                
                # Cancer of the soul
                sp.add_to_queue(uri='spotify:track:67biuNJA03k1cU0XpciTNJ',device_id=None)
                sleep(2)
                
            elif (id==620416664407):
                
                # 7/23
                sp.start_playback(device_id=None, context_uri='spotify:playlist:01aSPyH2lnYmW2CSqrKvYk')
                sleep(2)
                
            elif (id==963712058165):
                
                # Coffee Talk
                sp.start_playback(device_id=None, context_uri='spotify:playlist:6F3XvRKnH6RW8N9RbwlZ0C')
                sleep(2)
                
            elif (id==69939364845):
                
                # Hi im Gavin
                sp.start_playback(device_id=None, context_uri='spotify:playlist:5yUBBKEcFkeWbsceyAMmol')
                sleep(2)
                
            elif (id==951387022):
                
                # Liked Songs
                sp.start_playback(device_id=None, context_uri='spotify:playlist:1GW23LV3aK2sUO7L21UTzN')
                sleep(2)
                
                
            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
