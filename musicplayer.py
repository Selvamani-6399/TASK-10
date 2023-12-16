import random

class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def search_audio(self, name):
        for audio in self.audios:
            if audio.name == name:
                return audio
        return None

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        if len(self.ratings) == 0:
            return 0
        return sum(self.ratings) / len(self.ratings)

class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def search_playlist(self, name):
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist
        return None

    def generate_ratings(self):
        ratings = []
        for i in range(3):
            ratings.append(random.randint(1, 5))
        return ratings

if __name__ == '__main__':
    player = MusicPlayer()
    playlist1 = player.create_playlist('Rock', 'Rock')
    playlist2 = player.create_playlist('Pop', 'Pop')
    playlist3 = player.create_playlist('Jazz', 'Jazz')

    audio1 = Audio('Song1', 'https://www.example.com/song1.mp3')
    audio2 = Audio('Song2', 'https://www.example.com/song2.mp3')
    audio3 = Audio('Song3', 'https://www.example.com/song3.mp3')
    audio4 = Audio('Song4', 'https://www.example.com/song4.mp3')
    audio5 = Audio('Song5', 'https://www.example.com/song5.mp3')
    audio6 = Audio('Song6', 'https://www.example.com/song6.mp3')

    playlist1.add_audio(audio1)
    playlist1.add_audio(audio2)
    playlist1.add_audio(audio3)

    playlist2.add_audio(audio4)
    playlist2.add_audio(audio5)

    playlist3.add_audio(audio6)

    playlist1.add_rating(4)
    playlist1.add_rating(5)
    playlist1.add_rating(3)

    playlist2.add_rating(2)
    playlist2.add_rating(3)

    playlist3.add_rating(5)

    print(f'Average rating for {playlist1.name} is {playlist1.get_average_rating()}')
    print(f'Average rating for {playlist2.name} is {playlist2.get_average_rating()}')
    print(f'Average rating for {playlist3.name} is {playlist3.get_average_rating()}')
