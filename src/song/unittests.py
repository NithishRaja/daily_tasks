#
# File containing unit tests for song and lyric components
#
#

# Dependencies
import unittest
# Local Dependencies
from song import Song
from lyric import Lyric

class TestSongMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        self.songObj = Song()
    # Check get song for successful request
    def test_getSong_normal_response(self):
        attrList = ["title", "artist", "info"]
        res = self.songObj.getSongList()
        # Check if 100 songs have been returned
        self.assertTrue(len(res) == 100)
        # Check if song has all attributes
        for item in res[0].keys():
            self.assertTrue(item in attrList)
    # Check get song for response with multiple artists
    def test_getSong_multiple_artist_response(self):
        res = self.songObj.parseArtistString("abc x def & ghi + jkl featuring mno & pqr")
        # Check artist attribute
        self.assertTrue(len(res["artist"]) == 4)
        # Check featured attribute
        self.assertTrue(len(res["featured"]) == 2)
        # Check artists
        for item in res["artist"]:
            self.assertTrue(item in ["abc", "def", "ghi", "jkl"])
        # Check featured
        for item in res["featured"]:
            self.assertTrue(item in ["mno", "pqr"])
    # Check get song for failed request
    def test_getSong_failed_response(self):
        songObj = Song()
        songObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        res = songObj.getSongList()
        # Check if 100 songs have been returned
        self.assertTrue(len(songObj.getSongList()) == 0)
    # Tear down function
    def tearDown(self):
        del self.songObj

class TestLyricMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        self.lyricObj = Lyric()
    # Check get lyric for successful request
    def test_getLyric_normal_response(self):
        # Initialise title and artist
        title = "Bad Habits"
        artist = "Ed Sheeran"
        res = self.lyricObj.getLyric(title, artist)
        # Check result
        self.assertTrue(len(res) == 8)
    # Check get lyric for bad request
    def test_getLyric_empty_response(self):
        # Initialise title and artist
        title = ""
        artist = ""
        res = self.lyricObj.getLyric(title, artist)
        # Check result
        self.assertTrue(len(res) == 0)
    def test_getLyric_failed_response(self):
        # Initialise title and artist
        title = ""
        artist = ""
        lyricObj = Lyric()
        lyricObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        res = lyricObj.getLyric(title, artist)
        # Check result
        self.assertTrue(len(res) == 0)
    # Tear down function
    def tearDown(self):
        del self.lyricObj

if __name__ == "__main__":
    unittest.main()
