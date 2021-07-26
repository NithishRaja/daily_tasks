#
# File containing code for composer class
#
#

# Dependencies
import random
from datetime import date, timedelta

# Local Dependencies
from eventGetterInterface import EventGetterInterface
from quoteGetterInterface import QuoteGetterInterface
from songGetterInterface import SongGetterInterface
from videoGetterInterface import VideoGetterInterface
from scoreGetterInterface import ScoreGetterInterface
from wordGetterInterface import WordGetterInterface
from dayGetterInterface import DayGetterInterface
from tweetGetterInterface import TweetGetterInterface

# Initialise class
class Composer:
    # Initialise constructor
    def __init__(self):
        # Initialise variable to hold event getter
        self.eventGetter = None
        # Initialise variable to hold quote getter
        self.quoteGetter = None
        # Initialise variable to hold song getter
        self.songGetter = None
        # Initialise variable to hold video getter
        self.videoGetter = None
        # Initialise variable to hold score getter
        self.scoreGetter = None
        # Initialise variable to hold word getter
        self.wordGetter = None

    # Function to add event getter
    def addEventGetter(self, eventGetter: EventGetterInterface):
        """Store event getter object.

        Keyword Arguments:
        eventGetter -- object
        """
        self.eventGetter = eventGetter

    # Function to add quote getter
    def addQuoteGetter(self, quoteGetter: QuoteGetterInterface):
        """Store quote getter object.

        Keyword Arguments:
        quoteGetter -- object
        """
        self.quoteGetter = quoteGetter

    # Function to add song getter
    def addSongGetter(self, songGetter: SongGetterInterface):
        """Store song getter object.

        Keyword Arguments:
        songGetter -- object
        """
        self.songGetter = songGetter

    # Function to add video getter
    def addVideoGetter(self, videoGetter: VideoGetterInterface):
        """Store video getter object.

        Keyword Arguments:
        videoGetter -- object
        """
        self.videoGetter = videoGetter

    # Function to add score getter
    def addScoreGetter(self, scoreGetter: ScoreGetterInterface):
        """Store score getter object.

        Keyword Arguments:
        scoreGetter -- object
        """
        self.scoreGetter = scoreGetter

    # Function to add word getter
    def addWordGetter(self, wordGetter: WordGetterInterface):
        """Store word getter object.

        Keyword Arguments:
        wordGetter -- object
        """
        self.wordGetter = wordGetter

    # Function to add day getter
    def addDayGetter(self, dayGetter: DayGetterInterface):
        """Store day getter object.

        Keyword Arguments:
        dayGetter -- object
        """
        self.dayGetter = dayGetter

    # Function to add tweet getter
    def addTweetGetter(self, tweetGetter: TweetGetterInterface):
        """Store tweet getter object.

        Keyword Arguments:
        tweetGetter -- object
        """
        self.tweetGetter = tweetGetter

    # Function to extract event list from event getter
    def extractEvent(self):
        """Call getEvents function on eventGetter and return the result."""
        # Generate yesterday's date
        lowerLimit = date.today() - timedelta(days=1)
        # Generate date 10 days from today
        upperLimit = date.today() + timedelta(days=10)
        # Call function to get list of events and return it
        return self.eventGetter.getEvents(lowerLimit, upperLimit)

    # Function to extract quote from quote getter
    def extractQuote(self):
        """Call getQuoteList function on quoteGetter and return the result."""
        # Call function to get list of quotes
        res = self.quoteGetter.getQuoteList()
        # select a quote at random
        selectedQuote = random.choice(res["quotes"])
        # Return selected quote with topic
        return {
            "topic": res["topic"],
            "text": selectedQuote["text"],
            "author": selectedQuote["author"]
        }

    # Function to extract song from song getter
    def extractSong(self):
        """Get songs from song getter and corresponding video from video getter."""
        # Call function to get song
        selectedSong = self.songGetter.getSongsWithLyrics(1)[0]
        # Call function to get video URL for song
        videoURL = self.videoGetter.getVideoURL(selectedSong["title"]+" "+selectedSong["artist"]["artist"][0])
        # Call function to get lyric video URL for song
        lyricVideoURL = self.videoGetter.getVideoURL(selectedSong["title"]+" "+selectedSong["artist"]["artist"][0]+" lyrics")
        # Add video URLs to selected song
        selectedSong["video"] = {
            "watch": videoURL,
            "lyric": lyricVideoURL
        }
        # Return selected song
        return selectedSong

    # Function to extract score from score getter
    def extractScore(self):
        """Call getScoreByDay for current day."""
        return self.scoreGetter.getScoreByDay(self.scoreGetter.getCurrentDate())

    # Function to extract word from word getter
    def extractWord(self):
        """Call getWordWithMeaning and return the result."""
        return self.wordGetter.getWordWithMeaning()

    # Function to extract day from day getter
    def extractDay(self):
        """Call getDayByDate and get tweets for randomly chosen day."""
        # Call getDayByDate function
        res = self.dayGetter.getDayByDate(day=date.today().day, month=date.today().month)
        # Select a day at random
        selectedDay = random.choice(res)
        # Call function to get tweets
        selectedDay["tweet"] = self.tweetGetter.getTweetList(selectedDay["text"])
        # Return selected day with tweets
        return selectedDay
