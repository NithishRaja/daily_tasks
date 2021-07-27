#
# File containing code for composer class
#
#

# Dependencies
import random
from datetime import date, timedelta

# Local Dependencies
from getterFactory import GetterFactory
from persistenceInterface import PersistenceInterface

# Initialise class
class Composer:
    # Initialise constructor
    def __init__(self, getterFactory: GetterFactory, persistence: PersistenceInterface):
        # Initialise variable to hold getter factory
        self.getterFactory = getterFactory
        # Initialise variable to hold persistence object
        self.persistenceObj = persistence

    # Function to extract event list from event getter
    def extractEvent(self):
        """Call getEvents function on eventGetter and return the result."""
        # Retrieve event getter
        eventGetter = self.getterFactory.retrieveGetterByName("event")
        # Generate yesterday's date
        lowerLimit = date.today() - timedelta(days=1)
        # Generate date 10 days from today
        upperLimit = date.today() + timedelta(days=10)
        # Call function to get list of events and return it
        return eventGetter.getEvents(lowerLimit, upperLimit)

    # Function to extract quote from quote getter
    def extractQuote(self):
        """Call getQuoteList function on quoteGetter and return the result."""
        # Retrieve quote getter
        quoteGetter = self.getterFactory.retrieveGetterByName("quote")
        # Call function to get list of quotes
        res = quoteGetter.getQuoteList()
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
        # Retrieve song getter
        songGetter = self.getterFactory.retrieveGetterByName("song")
        # Retrieve video getter
        videoGetter = self.getterFactory.retrieveGetterByName("video")
        # Initialise variable to hold song
        selectedSong = None
        # Call function to get song
        res = songGetter.getSongsWithLyrics(1)
        # Check if response is empty
        if not len(res) == 0:
            selectedSong = res[0]
            # Call function to get video URL for song
            videoURL = videoGetter.getVideoURL(selectedSong["title"]+" "+selectedSong["artist"]["artist"][0])
            # Call function to get lyric video URL for song
            lyricVideoURL = videoGetter.getVideoURL(selectedSong["title"]+" "+selectedSong["artist"]["artist"][0]+" lyrics")
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
        # Retrieve score getter
        scoreGetter = self.getterFactory.retrieveGetterByName("score")
        # Return score
        return scoreGetter.getScoreByDay(scoreGetter.getCurrentDate())

    # Function to extract word from word getter
    def extractWord(self):
        """Call getWordWithMeaning and return the result."""
        # Retrieve word getter
        wordGetter = self.getterFactory.retrieveGetterByName("word")
        # Return word
        return wordGetter.getWordWithMeaning()

    # Function to extract day from day getter
    def extractDay(self):
        """Call getDayByDate and get tweets for randomly chosen day."""
        # Retrieve day getter
        dayGetter = self.getterFactory.retrieveGetterByName("day")
        # Retrieve tweet getter
        tweetGetter = self.getterFactory.retrieveGetterByName("tweet")
        # Initialise variable to hold randomly selected day
        selectedDay = None
        # Call getDayByDate function
        res = dayGetter.getDayByDate(day=date.today().day, month=date.today().month)
        # Check if response is empty
        if not len(res) == 0:
            # Select a day at random
            selectedDay = random.choice(res)
            # Call function to get tweets
            selectedDay["tweet"] = tweetGetter.getTweetList(selectedDay["text"])
        # Return selected day with tweets
        return selectedDay

    # Function to store data extracted from getters
    def execute(self):
        """Call extract functions and store the returned data."""
        # Store song data
        self.persistenceObj.persistDataByKey("song", self.extractSong())
        # Store event data
        self.persistenceObj.persistDataByKey("event", self.extractEvent())
        # Store quote data
        self.persistenceObj.persistDataByKey("quote", self.extractQuote())
        # Store score data
        self.persistenceObj.persistDataByKey("score", self.extractScore())
        # Store day data
        self.persistenceObj.persistDataByKey("day", self.extractDay())
        # Store word data
        self.persistenceObj.persistDataByKey("word", self.extractWord())
