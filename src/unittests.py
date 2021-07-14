#
# File containing unit tests
#
#

# Dependencies
import unittest, json, bs4
import sys

# adding src directory to the system path
sys.path.append('~/home/python/src/')

# Local Dependencies
from day import getDay
from quote import getQuote
from song import getSong
from tweet import getTweet
from words import getWords
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
file.close()

class TestHelperMethods(unittest.TestCase):
    # Check send_request function for 200 status code
    def test_send_request_for_status_code_200(self):
        res = send_request()["RAW"]("https://the-internet.herokuapp.com/status_codes/200")
        self.assertEqual(res["status"], 200)
    # Check send_request function for 404 status code
    def test_send_request_for_status_code_404(self):
        res = send_request()["RAW"]("https://the-internet.herokuapp.com/status_codes/404")
        self.assertEqual(res["status"], 404)
    # Check send_request function for 500 status code
    def test_send_request_for_status_code_500(self):
        res = send_request()["RAW"]("https://the-internet.herokuapp.com/status_codes/500")
        self.assertEqual(res["status"], 500)
    # Check send_request function for JSON payload
    def test_send_request_for_JSON_payload(self):
        res = send_request()["JSON"]("http://data.nba.net/10s/prod/v2/today.json")
        self.assertEqual(type(res["payload"]), type({}))
    # Check send_request function for HTML payload
    def test_send_request_for_HTML_payload(self):
        res = send_request()["HTML"]("https://the-internet.herokuapp.com/status_codes/200")
        self.assertEqual(type(res["payload"]), type( bs4.BeautifulSoup("", features="html.parser") ))

class TestMethods(unittest.TestCase):

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

    # Check output of getQuote function
    def test_quote(self):
        quote = getQuote()
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

    # Check output of getWords function
    def test_words(self):
        words = getWords()
        self.assertEqual(len(words), 2)
        for item in words:
            self.assertIs(type(item["word"]), type(""))
            self.assertIs(type(item["pronunciation"]), type(""))
            self.assertIs(type(item["wordType"]), type(""))
            self.assertIs(type(item["meaning"]), type([]))

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
