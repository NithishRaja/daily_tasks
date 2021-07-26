#
# File containing unit tests
#
#

# Dependencies
import unittest, requests, sys, os, json

sys.path.append(os.path.abspath(os.path.join("src")))
sys.path.append(os.path.abspath(os.path.join("src", "song")))
sys.path.append(os.path.abspath(os.path.join("src", "word")))

# Local Dependencies
from helpers.requestFacade import requestFacade
from composer import Composer
from event.eventGetter import EventGetter
from quote.quoteGetter import QuoteGetter
from song.songGetter import SongGetter
from song.song import Song
from song.lyric import Lyric
from video.videoGetter import VideoGetter
from score.scoreGetter import ScoreGetter
from word.wordGetter import WordGetter
from word.wordComposite import WordComposite
from word.meaning import Meaning
from word.dictionary import Dictionary
from word.merriam import Merriam
from day.dayGetter import DayGetter
from tweet.tweetGetter import TweetGetter

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

# Read config
file = open(os.path.join("credentials.json"))
credentials = json.load(file)
file.close()

class TestComposeMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise compose object
        self.composerObj = Composer()

    # Test getting events
    def test_composer_getting_events(self):
        # Add event getter
        self.composerObj.addEventGetter(EventGetter(os.path.join(sys.path[0], "testICS", "default.ics")))
        # Check output of extract event
        self.assertIs(type(self.composerObj.extractEvent()), type([]))

    # Test getting quote
    def test_composer_getting_quote(self):
        # Add quote getter
        self.composerObj.addQuoteGetter(QuoteGetter(requestFacade()))
        # Call extract quote function
        res = self.composerObj.extractQuote()
        # Check response type
        self.assertIs(type(res), type({}))
        # Check response attributes
        for item in res.keys():
            self.assertTrue(item in ["topic", "text", "author"])

    # Test getting song
    def test_composer_getting_song(self):
        # Add song getter
        self.composerObj.addSongGetter( SongGetter(Song(requestFacade()), Lyric(requestFacade())) )
        # Add video getter
        videoGetterObj = VideoGetter(requestFacade())
        videoGetterObj.addKey(credentials["youtube"]["APIKey"])
        self.composerObj.addVideoGetter(videoGetterObj)
        # Call extract song function
        res = self.composerObj.extractSong()
        # Check response type
        self.assertIs(type(res), type({}))
        # Check response attributes
        for item in res.keys():
            self.assertTrue(item in ["title", "artist", "info", "lyrics", "video"])

    # Test getting score
    def test_composer_getting_score(self):
        # Add score getter
        self.composerObj.addScoreGetter(ScoreGetter(requestFacade()))
        # Check output from extract score function
        self.assertIs(type(self.composerObj.extractScore()), type([]))

    # Test getting word
    def test_composer_getting_word(self):
        # Initialise word composite
        wordCompositeObj = WordComposite()
        # Initialise sender
        sender = requestFacade()
        # Add words to composite
        wordCompositeObj.addWord(Dictionary(sender))
        wordCompositeObj.addWord(Merriam(sender))
        # Add word getter
        self.composerObj.addWordGetter(WordGetter(wordCompositeObj, Meaning(sender)))
        # Call extract word function
        res = self.composerObj.extractWord()
        # Check output from extract word function
        self.assertIs(type(res), type([]))
        # Check attributes
        for resItem in res:
            for item in resItem.keys():
                self.assertTrue(item in ["word", "wordType", "pronunciation", "meaning"])

    # Test getting day
    def test_composer_getting_day(self):
        # Add day getter
        self.composerObj.addDayGetter(DayGetter(requestFacade()))
        # Add tweet getter
        tweetGetterObj = TweetGetter(requestFacade())
        tweetGetterObj.addToken(credentials["twitter"]["BearerToken"])
        self.composerObj.addTweetGetter(tweetGetterObj)
        # Call extract day function
        res = self.composerObj.extractDay()
        # Check output from extract day function
        self.assertIs(type(res), type({}))
        # Check attributes
        for item in res.keys():
            self.assertTrue(item in ["text", "link", "tweet"])

    # Tear down function
    def tearDown(self):
        del self.composerObj

if __name__ == "__main__":
    unittest.main()
