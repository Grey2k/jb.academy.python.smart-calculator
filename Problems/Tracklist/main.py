def tracklist(**artists):
    for artist, albums in artists.items():
        print(artist)
        for name, track in albums.items():
            print(f'ALBUM: {name} TRACK: {track}')
