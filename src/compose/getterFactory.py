#
# File containing code for getter factory class
#
#

# Dependencies

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
class GetterFactory:
    # Initialise constructor
    def __init__(self):
        # Initialise variable to hold all getters
        self.getterDict = {}

    # Function to add event getter
    def addEventGetter(self, eventGetter: EventGetterInterface):
        """Store event getter object.

        Keyword Arguments:
        eventGetter -- object
        """
        self.getterDict["event"] = eventGetter

    # Function to add quote getter
    def addQuoteGetter(self, quoteGetter: QuoteGetterInterface):
        """Store quote getter object.

        Keyword Arguments:
        quoteGetter -- object
        """
        self.getterDict["quote"] = quoteGetter

    # Function to add song getter
    def addSongGetter(self, songGetter: SongGetterInterface):
        """Store song getter object.

        Keyword Arguments:
        songGetter -- object
        """
        self.getterDict["song"] = songGetter

    # Function to add video getter
    def addVideoGetter(self, videoGetter: VideoGetterInterface):
        """Store video getter object.

        Keyword Arguments:
        videoGetter -- object
        """
        self.getterDict["video"] = videoGetter

    # Function to add score getter
    def addScoreGetter(self, scoreGetter: ScoreGetterInterface):
        """Store score getter object.

        Keyword Arguments:
        scoreGetter -- object
        """
        self.getterDict["score"] = scoreGetter

    # Function to add word getter
    def addWordGetter(self, wordGetter: WordGetterInterface):
        """Store word getter object.

        Keyword Arguments:
        wordGetter -- object
        """
        self.getterDict["word"] = wordGetter

    # Function to add day getter
    def addDayGetter(self, dayGetter: DayGetterInterface):
        """Store day getter object.

        Keyword Arguments:
        dayGetter -- object
        """
        self.getterDict["day"] = dayGetter

    # Function to add tweet getter
    def addTweetGetter(self, tweetGetter: TweetGetterInterface):
        """Store tweet getter object.

        Keyword Arguments:
        tweetGetter -- object
        """
        self.getterDict["tweet"] = tweetGetter

    # Function to return getter
    def retrieveGetterByName(self, name):
        """Return getter matching given string. If getter doesn't exits, return None.

        Keyword Arguments:
        name -- string
        """
        # Initialise variable for selected getter
        selectedGetter = None
        # Check if key exists in dict
        if name in self.getterDict.keys():
            selectedGetter = self.getterDict[name]
        # Return selected getter
        return selectedGetter
