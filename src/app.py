#
# File containing main logic
#
#

# Dependencies
import json, threading, os
from datetime import datetime, timedelta
# Local dependencies
from src.day import getDay
from src.quote import getQuote
from src.song import getSong
from src.tweet import getTweet
from src.score import getScore, getDate
from src.events import getEvents

class App:
    # Initialise constructor
    def __init__(self):

        # Initialise semaphore for cache
        self.cacheLock = threading.Semaphore()

        # Call function to read config
        self.readConfig()

        # Call function to read cache
        self.readCache()

        # Call function to read credentials
        self.readCredentials()

    def readConfig(self):
        # Read in configuration
        file = open("./config.json")
        # Parse JSON
        self.config = json.load(file)
        # Close file
        file.close()

    def readCache(self):
        # If cache file doesn't exists, create file
        if not os.path.isfile("./data/cache.json"):
            # Create file
            file = open("./data/cache.json", "w")
            # Create object with default values
            self.cache = {
                "day": [2021, 1, 1, 1],
                "quote": [2021, 1, 1, 1],
                "song": [2021, 1, 1, 1],
                "events": [2021, 1, 1],
                "score": {
                    "date": "20210101",
                    "status": False
                }
            }
            # Acquire lock
            self.cacheLock.acquire()
            # Write object to file
            json.dump(self.cache, file)
            # Close file
            file.close()
            # Release lock
            self.cacheLock.release()
        else:
            # Read in cache timers
            file = open("./data/cache.json")
            # Parse JSON
            self.cache = json.load(file)
            # Close file
            file.close()

    def readCredentials(self):
        # Read in configuration
        file = open("./credentials.json")
        # Parse JSON
        self.credentials = json.load(file)
        # Close file
        file.close()

    # Function to update day cache, if day cache has expired
    def day(self):
        # Get time of last data update
        lastUpdated = datetime(year=self.cache["day"][0], month=self.cache["day"][1], day=self.cache["day"][2], hour=self.cache["day"][3])
        # Get current time
        currentTime = datetime.now()
        # Get allowed time difference
        delta = timedelta(days=self.config["expiry"]["day"][0], seconds=self.config["expiry"]["day"][1], microseconds=self.config["expiry"]["day"][2])

        # Check if cache has expired
        if currentTime - lastUpdated > delta:
            # Call function to get day
            day = getDay()
            # Call function to get tweets
            tweets = getTweet(day["text"], self.credentials["twitter"]["BearerToken"], self.config["tweetCount"]["day"])
            # Add tweets to day object
            day["tweets"] = tweets
            # Open file
            file = open("./data/day.json", "w")
            # Write to file
            json.dump(day, file)
            # Close file
            file.close()

            # Acquire lock
            self.cacheLock.acquire()
            # Update cache timer
            file = open("./data/cache.json", "w")
            # Update cache with current time data
            self.cache["day"] = [currentTime.year, currentTime.month, currentTime.day, currentTime.hour]
            # Write to file
            json.dump(self.cache, file)
            # Close file
            file.close()
            # Release lock
            self.cacheLock.release()

    # Function to update quote cache, if cache has expired
    def quote(self):
        # Get time of last data update
        lastUpdated = datetime(year=self.cache["quote"][0], month=self.cache["quote"][1], day=self.cache["quote"][2], hour=self.cache["quote"][3])
        # Get current time
        currentTime = datetime.now()
        # Get allowed time difference
        delta = timedelta(days=self.config["expiry"]["quote"][0], seconds=self.config["expiry"]["quote"][1], microseconds=self.config["expiry"]["quote"][2])

        # Check if cache has expired
        if currentTime - lastUpdated > delta:
            # Call function to get quote
            quote = getQuote()
            # Open file
            file = open("./data/quote.json", "w")
            # Write to file
            json.dump(quote, file)
            # Close file
            file.close()

            # Acquire lock
            self.cacheLock.acquire()
            # Update cache timer
            file = open("./data/cache.json", "w")
            # Update cache with current time data
            self.cache["quote"] = [currentTime.year, currentTime.month, currentTime.day, currentTime.hour]
            # Write to file
            json.dump(self.cache, file)
            # Close file
            file.close()
            # Release lock
            self.cacheLock.release()

    # Function to update song cache, if cache has expired
    def song(self):
        # Get time of last data update
        lastUpdated = datetime(year=self.cache["song"][0], month=self.cache["song"][1], day=self.cache["song"][2], hour=self.cache["song"][3])
        # Get current time
        currentTime = datetime.now()
        # Get allowed time difference
        delta = timedelta(days=self.config["expiry"]["song"][0], seconds=self.config["expiry"]["song"][1], microseconds=self.config["expiry"]["song"][2])

        # Check if cache has expired
        if currentTime - lastUpdated > delta:
            # Call function to get song
            song = getSong(self.credentials["youtube"]["APIKey"])
            # Open file
            file = open("./data/song.json", "w")
            # Write to file
            json.dump(song, file)
            # Close file
            file.close()

            # Acquire lock
            self.cacheLock.acquire()
            # Update cache timer
            file = open("./data/cache.json", "w")
            # Update cache with current time data
            self.cache["song"] = [currentTime.year, currentTime.month, currentTime.day, currentTime.hour]
            # Write to file
            json.dump(self.cache, file)
            # Close file
            file.close()
            # Release lock
            self.cacheLock.release()

    # Function to get score
    def score(self):
        # Check if cache is up to date
        if not (self.cache["score"]["date"] == getDate() and self.cache["score"]["status"]):
            # Call function to get score
            score = getScore()
            # Open file
            file = open("./data/score.json", "w")
            # Write to file
            json.dump(score, file)
            # Close file
            file.close()

            # Acquire lock
            self.cacheLock.acquire()
            # Update cache timer
            file = open("./data/cache.json", "w")
            # Update cache with current time data
            self.cache["score"]["date"] = score["currentDate"]
            self.cache["score"]["status"] = score["cache"]
            # Write to file
            json.dump(self.cache, file)
            # Close file
            file.close()
            # Release lock
            self.cacheLock.release()

    # Function to get events
    def events(self):
        # Get time of last data update
        lastUpdated = datetime(year=self.cache["events"][0], month=self.cache["events"][1], day=self.cache["events"][2])
        # Get current time
        currentTime = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)

        # Check if cache is up to date
        if not lastUpdated == currentTime:
            # Call function to get score
            events = getEvents(self.config["calendar"]["fileName"], self.config["calendar"]["upperLimit"], self.config["calendar"]["lowerLimit"])
            # Open file
            file = open("./data/events.json", "w")
            # Write to file
            json.dump(events, file)
            # Close file
            file.close()

            # Acquire lock
            self.cacheLock.acquire()
            # Update cache timer
            file = open("./data/cache.json", "w")
            # Update cache with current time data
            self.cache["events"] = [currentTime.year, currentTime.month, currentTime.day]
            # Write to file
            json.dump(self.cache, file)
            # Close file
            file.close()
            # Release lock
            self.cacheLock.release()
