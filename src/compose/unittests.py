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
from getterFactory import GetterFactory
from persistence.persistInMemory import PersistInMemory
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
        # Initialise sender
        sender = requestFacade()
        # Initialise getter factory
        getterFactory = GetterFactory()
        # Add event getter
        getterFactory.addEventGetter(EventGetter(os.path.join(sys.path[0], "testICS", "default.ics")))
        # Add quote getter
        getterFactory.addQuoteGetter(QuoteGetter(sender))
        # Add song getter
        getterFactory.addSongGetter( SongGetter(Song(sender), Lyric(sender)) )
        # Add video getter
        videoGetterObj = VideoGetter(requestFacade())
        videoGetterObj.addKey(credentials["youtube"]["APIKey"])
        getterFactory.addVideoGetter(videoGetterObj)
        # Add score getter
        getterFactory.addScoreGetter(ScoreGetter(sender))
        # Initialise word composite
        wordCompositeObj = WordComposite()
        # Add words to composite
        wordCompositeObj.addWord(Dictionary(sender))
        wordCompositeObj.addWord(Merriam(sender))
        # Add word getter
        getterFactory.addWordGetter(WordGetter(wordCompositeObj, Meaning(sender)))
        # Add day getter
        getterFactory.addDayGetter(DayGetter(sender))
        # Add tweet getter
        tweetGetterObj = TweetGetter(sender)
        tweetGetterObj.addToken(credentials["twitter"]["BearerToken"])
        getterFactory.addTweetGetter(tweetGetterObj)

        # Initialise persist in memory object
        self.persistInMemoryObj = PersistInMemory()
        # Initialise compose object
        self.composerObj = Composer(getterFactory, self.persistInMemoryObj)

    # Test getting events
    def test_composer_getting_events(self):
        # Check output of extract event
        self.assertIs(type(self.composerObj.extractEvent()), type([]))

    # Test getting quote
    def test_composer_getting_quote(self):
        # Call extract quote function
        res = self.composerObj.extractQuote()
        # Check response type
        self.assertIs(type(res), type({}))
        # Check response attributes
        for item in res.keys():
            self.assertTrue(item in ["topic", "text", "author"])

    # Test getting song success
    def test_composer_getting_song_success(self):
        # Call extract song function
        res = self.composerObj.extractSong()
        # Check response type
        self.assertIs(type(res), type({}))
        # Check response attributes
        for item in res.keys():
            self.assertTrue(item in ["title", "artist", "info", "lyrics", "video"])

    # Test getting song failure
    def test_composer_getting_song_failure(self):
        # Initialise getter factory
        getterFactory = GetterFactory()
        # Add song getter
        getterFactory.addSongGetter( SongGetter(Song(simulationFacade()), Lyric(simulationFacade())) )
        # Add video getter
        videoGetterObj = VideoGetter(requestFacade())
        videoGetterObj.addKey(credentials["youtube"]["APIKey"])
        getterFactory.addVideoGetter(videoGetterObj)
        # Add getter factory to composer
        self.composerObj.getterFactory = getterFactory
        # Check response type
        self.assertEqual(self.composerObj.extractSong(), None)

    # Test getting score
    def test_composer_getting_score(self):
        # Check output from extract score function
        self.assertIs(type(self.composerObj.extractScore()), type([]))

    # Test getting word
    def test_composer_getting_word(self):
        # Call extract word function
        res = self.composerObj.extractWord()
        # Check output from extract word function
        self.assertIs(type(res), type([]))
        # Check attributes
        for resItem in res:
            for item in resItem.keys():
                self.assertTrue(item in ["word", "wordType", "pronunciation", "meaning"])

    # Test getting day success
    def test_composer_getting_day_success(self):
        # Call extract day function
        res = self.composerObj.extractDay()
        # Check output from extract day function
        self.assertIs(type(res), type({}))
        # Check attributes
        for item in res.keys():
            self.assertTrue(item in ["text", "link", "tweet"])

    # Test getting day failure
    def test_composer_getting_day_failure(self):
        # Initialise getter factory
        getterFactory = GetterFactory()
        # Add day getter
        getterFactory.addDayGetter(DayGetter(simulationFacade()))
        # Add tweet getter
        tweetGetterObj = TweetGetter(requestFacade())
        tweetGetterObj.addToken(credentials["twitter"]["BearerToken"])
        getterFactory.addTweetGetter(tweetGetterObj)
        # Add getter factory to composer
        self.composerObj.getterFactory = getterFactory
        # Check output from extract day function
        self.assertEqual(self.composerObj.extractDay(), None)

    # Test persistence
    def test_composer_persistence(self):
        # Call execute function
        self.composerObj.execute()

        # Check song data in persistence
        songRes = self.persistInMemoryObj.retrieveDataByKey("song")
        # Check response type
        self.assertIs(type(songRes), type({}))
        # Check response attributes
        for item in songRes.keys():
            self.assertTrue(item in ["title", "artist", "info", "lyrics", "video"])

        # Check event data in persistence
        eventRes = self.persistInMemoryObj.retrieveDataByKey("event")
        # Check response type
        self.assertIs(type(eventRes), type([]))

        # Check quote data in persistence
        quoteRes = self.persistInMemoryObj.retrieveDataByKey("quote")
        # Check response type
        self.assertIs(type(quoteRes), type({}))
        # Check response attributes
        for item in quoteRes.keys():
            self.assertTrue(item in ["topic", "text", "author"])

        # Check score data in persistence
        scoreRes = self.persistInMemoryObj.retrieveDataByKey("score")
        # Check response type
        self.assertIs(type(scoreRes), type([]))

        # Check day data in persistence
        dayRes = self.persistInMemoryObj.retrieveDataByKey("day")
        # Check response type
        self.assertIs(type(dayRes), type({}))
        # Check attributes
        for item in dayRes.keys():
            self.assertTrue(item in ["text", "link", "tweet"])

        # Check word data in persistence
        wordRes = self.persistInMemoryObj.retrieveDataByKey("word")
        # Check response type
        self.assertIs(type(wordRes), type([]))
        # Check attributes
        for resItem in wordRes:
            for item in resItem.keys():
                self.assertTrue(item in ["word", "wordType", "pronunciation", "meaning"])

    # Tear down function
    def tearDown(self):
        del self.composerObj
        del self.persistInMemoryObj

if __name__ == "__main__":
    unittest.main()
