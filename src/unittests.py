#
# File containing unit tests
#
#

# Dependencies
import unittest, json
# Local Dependencies
from day import getDay
from quote import getQuote
from song import getSong
from tweet import getTweet
from words import Words
from events import getEvents
from score import getScore
from helpers.sendRequests import send_request

# Read in credentials
file = open("./credentials.json")
credentials = json.load(file)
file.close()

# Read in credentials
file = open("./config.json")
config = json.load(file)
quote = getQuote()
file.close()

class TestDayMethods(unittest.TestCase):
    # Check output of getDay function for normal request
    def test_day_normal_response(self):
        # Initialise array to hold titles
        titles = ["French Fries Day", "Cow Appreciation Day", "Beef Tallow Day", "International Rock Day", "Bubblegum Day", "Embrace Your Geekness Day"]
        # Call function
        dayList = getDay(day=13, month=7)
        # Check length of array
        self.assertEqual(len(dayList), 6)
        # Check elements of array
        for item in dayList:
            self.assertTrue(item["text"] in titles)
    # Check output of getDay function for bad request
    def test_day_empty_response(self):
        # Call function with bad parameters
        dayList = getDay(day=-1, month=-1)
        # Check length of array
        self.assertEqual(len(dayList), 0)

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

class TestMethods(unittest.TestCase):
    # Check output of getQuote function
    def test_quote(self):
        self.assertIs(type(quote["topic"]), type(""))
        self.assertIs(type(quote["quote"]), type(""))
        self.assertIs(type(quote["author"]), type(""))

    # Check output of getSong function
    def test_song(self):
        song = getSong(credentials["youtube"]["APIKey"])
        self.assertIs(type(song["title"]), type(""))
        self.assertIs(type(song["artist"]), type(""))
        self.assertIs(type(song["info"]), type([]))
        self.assertIs(type(song["lyrics"]), type([]))
        self.assertIs(type(song["video"]), type({}))

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

    # Check output of getEvents function
    def test_events(self):
        events = getEvents(config["calendar"]["fileName"], config["calendar"]["upperLimit"], config["calendar"]["lowerLimit"])
        self.assertEqual(type(events), type([]))

    # Check output of getScore function
    def test_score(self):
        score = getScore()
        self.assertEqual(type(score), type({}))

if __name__ == '__main__':
    unittest.main()
