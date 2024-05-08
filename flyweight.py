class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

song_data = {
    "Saharna Ya Leil": Song("Saharna Ya Leil", "Elisa", "4:16"),
    "Momento": Song("Momento", "The Ab Brothers", "4:05"),
    "Aoul Ansak": Song("Aoul Ansak", "Carole Samaha", "3:36")
}

playlists = [
    Playlist("Workout Playlist"),
    Playlist("Chill Playlist"),
    Playlist("Party Playlist")
]

playlists[0].add_song(song_data["Saharna Ya Leil"])
playlists[1].add_song(song_data["Momento"])
playlists[2].add_song(song_data["Aoul Ansak"])
