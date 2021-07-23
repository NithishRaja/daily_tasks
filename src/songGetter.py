#
# File to get a random song
#
#

# Dependencies
import random
# Local Dependencies
from getterInterface import GetterInterface
from song.song import Song
from song.lyric import Lyric

class SongGetter(GetterInterface):
    def __init__(self):
        # Initialise song object
        self.song = Song()
        # Initialise lyric object
        self.lyric = Lyric()
        # Initialise array to hold songs
        self.songList = []
        # Call function to populate song list
        self.populateSongList()

    # Function to populate song list
    def populateSongList(self):
        # Call function to get songs
        temp = self.song.getSongList()
        # Check song list length
        if not len(temp) == 0:
            self.songList = temp

    # Function to get a random song
    def getData(self):
        # Initialise object to hold song
        result = {}
        # Check song list length
        if not len(self.songList) == 0:
            # Select song at random
            result = self.songList[ random.randint(0, len(self.songList)-1) ]
            # Call function to get lyrics of song
            result["lyrics"] = self.lyric.getLyric(result["title"], result["artist"]["artist"][0])
        # Return result
        return result
