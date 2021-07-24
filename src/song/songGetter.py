#
# File to get a random song
#
#

# Dependencies
import random
# Local Dependencies
from songGetterInterface import SongGetterInterface
from lyricInterface import LyricInterface
from songInterface import SongInterface

class SongGetter(SongGetterInterface):
    def __init__(self, song: SongInterface, lyric: LyricInterface):
        # Initialise song object
        self.song = song
        # Initialise lyric object
        self.lyric = lyric
        # Initialise array to hold songs
        self.songList = []
        # Call function to populate song list
        self.populateSongList()
        # Call function to randomise song list
        self.randomizeSongList()

    # Function to populate song list
    def populateSongList(self):
        """Call function in Song class to get list of songs."""
        # Call function to get songs
        temp = self.song.getSongList()
        # Check song list length
        if not len(temp) == 0:
            self.songList = temp

    # Function to randomize song list
    def randomizeSongList(self):
        """Shuffle the elements in song list."""
        random.shuffle(self.songList)

    # Function to get random songs with lyrics
    def getSongsWithLyrics(self, maxCount):
        """Get lyrics for songs up till max count. Return songs with their lyrics.

        Keyword Arguments:
        maxCount -- integer
        """
        # Initialise list to hold songs
        result = []
        # Check song list length
        if not len(self.songList) == 0:
            # Initialise counter
            counter = 0
            # Iterate till counter reached max count
            while counter < maxCount and counter < len(self.songList):
                # Update counter
                counter = counter + 1
                # Select song
                selectedSong = self.songList[counter]
                # Get lyrics of selected song
                selectedSong["lyrics"] = self.lyric.getLyric(selectedSong["title"], selectedSong["artist"]["artist"][0])
                # Append selected song to result
                result.append(selectedSong)
        # Return result
        return result
