#
# File containing unit tests
#
#

# Dependencies
import unittest, json
# Local Dependencies
from day import Day
from quoteGetter import QuoteGetter
from songGetter import SongGetter
from eventGetter import EventGetter
from tweet import getTweet
from words import Words
from scoreGetter import ScoreGetter

# Read in credentials
file = open("./credentials.json")
credentials = json.load(file)
file.close()

# Read in credentials
file = open("./config.json")
config = json.load(file)
file.close()

class TestDayMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise day object
        self.dayObj = Day()
    # Check output of getDay function for normal request
    def test_day_normal_response(self):
        # Call function to get data
        dayList = self.dayObj.getData()
        # Check length of array
        self.assertTrue(len(dayList) > 0)
    # Check output of getDay function for normal specified request
    def test_day_specified_date(self):
        # Initialise array to hold titles
        titles = ["French Fries Day", "Cow Appreciation Day", "Beef Tallow Day", "International Rock Day", "Bubblegum Day", "Embrace Your Geekness Day"]
        # Call function to set date
        self.dayObj.setDate(day=13, month=7)
        # Call function to get data
        dayList = self.dayObj.getData()
        # Check length of array
        self.assertEqual(len(dayList), 6)
        # Check elements of array
        for item in dayList:
            self.assertTrue(item["text"] in titles)
    # Check output of getDay function for bad request
    def test_day_empty_response(self):
        # Call function to set date
        self.dayObj.setDate(day=-1, month=-1)
        # Call function to get data
        dayList = self.dayObj.getData()
        # Check length of array
        self.assertEqual(len(dayList), 0)
    # Tear down function
    def tearDown(self):
        del self.dayObj

class TestWordMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise word object
        self.wordObj = Words()
    # Check output of words class for normal request
    def test_words_normal_response(self):
        # Call function to get data
        words = self.wordObj.getData()
        # Check number of words returned
        self.assertEqual(len(words), 2)
        for item in words:
            self.assertEqual(type(item["word"]), type(""))
            self.assertEqual(type(item["pronunciation"]), type(""))
            self.assertEqual(type(item["wordType"]), type(""))
            self.assertTrue(len(item["meaning"]) > 0)
    # Check output of words class for bad request
    def test_words_failed_response(self):
        # Initialise word object
        wordObj = Words()
        # Update URLs
        wordObj.merriam_webster_url = "https://the-internet.herokuapp.com/status_codes/404"
        wordObj.dictionary_url = "https://the-internet.herokuapp.com/status_codes/404"
        # Call function to get data
        words = wordObj.getData()
        # Check number of objects returned
        self.assertEqual(len(words), 0)
    # Check output of getMeaning for successful request
    def test_getMeaning_for_normal_response(self):
        # Initialise array of meanings
        meanings = [': to destroy to the ground : demolish', ': to scrape, cut, or shave off', ': erase']
        # Call function to get meanings
        data = self.wordObj.getMeaning("raze")
        # Check number of entries in data returned
        self.assertEqual(len(data), 3)
        # Check data
        for item in data:
            self.assertTrue(item in meanings)
    # Check output of getMeaning for bad request
    def test_getMeaning_for_bad_response(self):
        # Call function to get meanings
        data = self.wordObj.getMeaning("hoping this is not a word")
        self.assertEqual(len(data), 0)
    # Check output of getMeaning for failed request
    def test_getMeaning_for_no_response(self):
        wordObj = Words()
        wordObj.merriam_webster_url = "https://the-internet.herokuapp.com/status_codes/404"
        # Call function to get meanings
        data = wordObj.getMeaning("does not matter")
        self.assertEqual(len(data), 0)
    # Tear down function
    def tearDown(self):
        del self.wordObj

class TestQuoteGetterMethods(unittest.TestCase):
    # Set up fuction
    def setUp(self):
        self.quoteGetterObj = QuoteGetter()
    # Check quote getter for successful request
    def test_quote_getter_getData_on_success(self):
        # Initialise list of fileds in quote data
        quoteFields = ["text", "topic", "author"]
        # Call function to get quote data
        res = self.quoteGetterObj.getData()
        # Check response type
        self.assertIs(type(res), type({}))
        # Check fields of object
        for item in res.keys():
            self.assertTrue(item in quoteFields)
    # Check quote getter for failed request
    def test_quote_getter_getData_on_failure(self):
        # Initialise default quote object
        defaultQuote = {
            "text": "To refactor or to start from scratch?",
            "author": "Cocoa Puffs",
        }
        # Initialise quoteGetter object
        quoteGetterObj = QuoteGetter()
        quoteGetterObj.quoteList = []
        # Call function to get quote data
        res = quoteGetterObj.getData()
        # Check response
        for item in defaultQuote.keys():
            self.assertEqual(res[item], defaultQuote[item])
    # Tear down function
    def tearDown(self):
        del self.quoteGetterObj

class TestSongGetterMethods(unittest.TestCase):
    # Set up fuction
    def setUp(self):
        self.songGetterObj = SongGetter()
    # Check song getter for successful request
    def test_song_getter_getData_on_success(self):
        # Initialise list of fileds in song data
        quoteFields = ["title", "artist", "info", "lyrics"]
        # Call function to get song data
        res = self.songGetterObj.getData()
        # Check response type
        self.assertIs(type(res), type({}))
        # Check fields of object
        for item in res.keys():
            self.assertTrue(item in quoteFields)
    # Check song getter for failed request
    def test_song_getter_getData_on_failure(self):
        songGetterObj = SongGetter()
        songGetterObj.songList = []
        # Call function to get song data
        res = songGetterObj.getData()
        # Check response
        self.assertEqual(res, {})
    # Tear down function
    def tearDown(self):
        del self.songGetterObj

class TestEventGetterMethods(unittest.TestCase):
    # Set up fuction
    def setUp(self):
        self.eventGetterObj = EventGetter()
    # Check get data
    def test_event_getter_getData(self):
        # Check response
        self.assertEqual(type(self.eventGetterObj.getData()), type([]))
    # Tear down function
    def tearDown(self):
        del self.eventGetterObj

class TestScoreGetterMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise object
        self.scoreGetterObj = ScoreGetter()
    # Check get data
    def test_score_geter_getData(self):
        # Initialise attribute list
        attributeList = ["currentDate", "standingsURL", "games"]
        # Get data
        res = self.scoreGetterObj.getData()
        # Check attributes
        for item in attributeList:
            self.assertTrue(item in res.keys())
    # Tear down function
    def tearDown(self):
        del self.scoreGetterObj

class TestMethods(unittest.TestCase):
    # Check output of getTweet function
    def test_tweet(self):
        count = 1
        tweets = getTweet("nba", credentials["twitter"]["BearerToken"], count)
        self.assertEqual(len(tweets), count)
        for item in tweets:
            self.assertIs(type(item["text"]), type([]))
            self.assertIs(type(item["name"]), type(""))
            self.assertIs(type(item["username"]), type(""))
            self.assertIs(type(item["profile_image_url"]), type(""))
            self.assertIs(type(item["profile_url"]), type(""))
            self.assertIs(type(item["tweet_url"]), type(""))

if __name__ == '__main__':
    unittest.main()
