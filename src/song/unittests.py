#
# File containing unit tests for song and lyric components
#
#

# Dependencies
import unittest, requests, sys, os

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from helpers.requestFacade import requestFacade
from song import Song
from lyric import Lyric
from songGetter import SongGetter

def simulate_failed_response(url):
    res = requests.get("https://the-internet.herokuapp.com/status_codes/404")
    return {
        "status": res.status_code,
        "payload": res.text
    }

def simulationFacade():
    return {
        "HTML": simulate_failed_response
    }

class TestSongMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        self.songObj = Song(requestFacade())
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
        self.songObj.sender = simulationFacade()
        # Get response
        res = self.songObj.getSongList()
        # Check length of response
        self.assertTrue(len(res) == 0)
    # Tear down function
    def tearDown(self):
        del self.songObj

class TestLyricMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        self.lyricObj = Lyric(requestFacade())
    # Check get lyric for successful request
    def test_getLyric_normal_response(self):
        # Initialise title and artist
        title = "Bad Habits"
        artist = "Ed Sheeran"
        # Get response
        res = self.lyricObj.getLyric(title, artist)
        # Check result
        self.assertTrue(len(res) == 8)
    # Check get lyric for bad request
    def test_getLyric_empty_response(self):
        # Initialise title and artist
        title = ""
        artist = ""
        # Get response
        res = self.lyricObj.getLyric(title, artist)
        # Check result
        self.assertTrue(len(res) == 0)
    def test_getLyric_failed_response(self):
        # Initialise title and artist
        title = ""
        artist = ""
        # Update sender
        self.lyricObj.sender = simulationFacade()
        # Get response
        res = self.lyricObj.getLyric(title, artist)
        # Check result
        self.assertTrue(len(res) == 0)
    # Tear down function
    def tearDown(self):
        del self.lyricObj

class TestSongGetterMethods(unittest.TestCase):
    # Set up fuction
    def setUp(self):
        self.songGetterObj = SongGetter(Song(requestFacade()), Lyric(requestFacade()))
    # Check song getter for successful request
    def test_song_getter_getData_on_success(self):
        # Initialise list of fileds in song data
        attributeList = ["title", "artist", "info", "lyrics"]
        # Initialise count
        count = 2
        # Call function to get song data
        res = self.songGetterObj.getSongsWithLyrics(count)
        # Check response type
        self.assertIs(type(res), type([]))
        # Check response length
        self.assertEqual(len(res), count)
        # Iterate over elements in response
        for resItem in res:
            # Check fields of object
            for item in resItem.keys():
                self.assertTrue(item in attributeList)
    # Check song getter for failed request
    def test_song_getter_getData_on_failure(self):
        # Replace populated song list with empty list
        self.songGetterObj.songList = []
        # Call function to get song data
        res = self.songGetterObj.getSongsWithLyrics(1)
        # Check response
        self.assertEqual(res, [])
        # Check response length
        self.assertEqual(len(res), 0)
    # Tear down function
    def tearDown(self):
        del self.songGetterObj

if __name__ == "__main__":
    unittest.main()
