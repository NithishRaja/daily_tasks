import unittest, json
from src.day import getDay
from src.quote import getQuote
from src.song import getSong
from src.tweet import getTweet
from src.words import getWords
from src.events import getEvents
from src.score import getScore

# Read in credentials
file = open("./credentials.json")
credentials = json.load(file)
file.close()

# Read in credentials
file = open("./config.json")
config = json.load(file)
file.close()

class TestStringMethods(unittest.TestCase):

    # Check output of getDay function
    def test_day(self):
        day = getDay()
        self.assertIs(type(day["text"]), type(""))
        self.assertIs(type(day["link"]), type(""))

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
