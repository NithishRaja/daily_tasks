#
# File containing code to initialise all classes
#
#

# Dependencies
import sys, os, json

sys.path.append(os.path.abspath(os.path.join("src")))
sys.path.append(os.path.abspath(os.path.join("src", "compose")))
sys.path.append(os.path.abspath(os.path.join("src", "song")))
sys.path.append(os.path.abspath(os.path.join("src", "word")))

# Local Dependencies
from helpers.requestFacade import requestFacade
from compose.composer import Composer
from compose.getterFactory import GetterFactory
from song.songGetter import SongGetter
from song.song import Song
from song.lyric import Lyric
from video.videoGetter import VideoGetter
from event.eventGetter import EventGetter
from quote.quoteGetter import QuoteGetter
from score.scoreGetter import ScoreGetter
from tweet.tweetGetter import TweetGetter
from day.dayGetter import DayGetter
from word.wordGetter import WordGetter
from word.wordComposite import WordComposite
from word.meaning import Meaning
from word.dictionary import Dictionary
from word.merriam import Merriam
from persistence.persistInMemory import PersistInMemory
from UI.webUI import WebUI

# Read credentials
file = open(os.path.join("credentials.json"))
credentials = json.load(file)
file.close()

# Read config
file = open(os.path.join("config.json"))
config = json.load(file)
file.close()

# Initialise sender
sender = requestFacade()
# Initialise getter factory
getterFactory = GetterFactory()

# Add song getter
getterFactory.addSongGetter( SongGetter(Song(sender), Lyric(sender)) )

# Add video getter
videoGetterObj = VideoGetter(requestFacade())
videoGetterObj.addKey(credentials["youtube"]["APIKey"])
getterFactory.addVideoGetter(videoGetterObj)

# Add event getter
getterFactory.addEventGetter(EventGetter(os.path.join("userData", config["calendar"]["fileName"])))

# Add quote getter
getterFactory.addQuoteGetter(QuoteGetter(sender))

# Add score getter
getterFactory.addScoreGetter(ScoreGetter(sender))

# Add day getter
getterFactory.addDayGetter(DayGetter(sender))

# Add tweet getter
tweetGetterObj = TweetGetter(sender)
tweetGetterObj.addToken(credentials["twitter"]["BearerToken"])
getterFactory.addTweetGetter(tweetGetterObj)

# Initialise word composite
wordCompositeObj = WordComposite()
# Add words to composite
wordCompositeObj.addWord(Dictionary(sender))
wordCompositeObj.addWord(Merriam(sender))
# Add word getter
getterFactory.addWordGetter(WordGetter(wordCompositeObj, Meaning(sender)))

# Initialise persistence
persistence = PersistInMemory()

# Initialise composer
composer = Composer(getterFactory, persistence, WebUI(persistence))

# Call execute on composer
composer.execute()
