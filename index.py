#
# Index File
#
#

# Dependencies
import json, threading, os
from datetime import datetime, timedelta
# Local dependencies
from src.day import getDay
from src.quote import getQuote
from src.song import getSong

# Function to update day cache, if day cache has expired
def day():
    # Get time of last data update
    lastUpdated = datetime(year=cache["day"][0], month=cache["day"][1], day=cache["day"][2], hour=cache["day"][3])
    # Get current time
    currentTime = datetime.now()
    # Get allowed time difference
    delta = timedelta(days=config["expiry"]["day"][0], seconds=config["expiry"]["day"][1], microseconds=config["expiry"]["day"][2])
    # Check if cache has expired
    if currentTime - lastUpdated > delta:
        # Iterate till request is a success
        while(True):
            try:
                # Call function to get day
                day = getDay()
                # Open file
                file = open("./data/day.json", "w")
                # Write to file
                json.dump(day, file)
                # Close file
                file.close()
                # Update cache timer
                # Exit loop
                break
            except:
                # Print error message
                print("Failed to get day. Trying again...")

# Function to update quote cache, if cache has expired
def quote():
    # Get time of last data update
    lastUpdated = datetime(year=cache["quote"][0], month=cache["quote"][1], day=cache["quote"][2], hour=cache["quote"][3])
    # Get current time
    currentTime = datetime.now()
    # Get allowed time difference
    delta = timedelta(days=config["expiry"]["quote"][0], seconds=config["expiry"]["quote"][1], microseconds=config["expiry"]["quote"][2])
    # Check if cache has expired
    if currentTime - lastUpdated > delta:
        # Iterate till request is a success
        while(True):
            try:
                # Call function to get quote
                quote = getQuote()
                # Open file
                file = open("./data/quote.json", "w")
                # Write to file
                json.dump(quote, file)
                # Close file
                file.close()
                # Exit loop
                break
            except:
                # Print error message
                print("Failed to get quote. Trying again...")

# Function to update song cache, if cache has expired
def song():
    # Get time of last data update
    lastUpdated = datetime(year=cache["song"][0], month=cache["song"][1], day=cache["song"][2], hour=cache["song"][3])
    # Get current time
    currentTime = datetime.now()
    # Get allowed time difference
    delta = timedelta(days=config["expiry"]["song"][0], seconds=config["expiry"]["song"][1], microseconds=config["expiry"]["song"][2])
    # Check if cache has expired
    if currentTime - lastUpdated > delta:
        # Iterate till request is a success
        while(True):
            try:
                # Call function to get song
                song = getSong()
                # Open file
                file = open("./data/song.json", "w")
                # Write to file
                json.dump(song, file)
                # Close file
                file.close()
                # Exit loop
                break
            except:
                # Print error message
                print("Failed to get song. Trying again...")

# Check if cache file exists
if not os.path.isfile("./data/cache.json"):
    # Create file
    file = open("./data/cache.json", "w")
    # Create empty object
    cache = {
        "day": [2021, 1, 1, 1],
        "quote": [2021, 1, 1, 1],
        "song": [2021, 1, 1, 1]
    }
    # Write object to file
    json.dump(cache, file)
    # Close file
    file.close()

# Read in configuration
file = open("./config.json")
# Parse JSON
config = json.load(file)
# Close file
file.close()

# Read in cache timers
file = open("./data/cache.json")
# Parse JSON
cache = json.load(file)
# Close file
file.close()

# Initialise threads
dayThread = threading.Thread(target=day, args=[])
quoteThread = threading.Thread(target=quote, args=[])
songThread = threading.Thread(target=song, args=[])

# Start threads
dayThread.start()
quoteThread.start()
songThread.start()
