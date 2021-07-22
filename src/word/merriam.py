#
# File containing class for getting word from dictionary.com
#
#

# Dependencies
import sys, os

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from wordInterface import WordInterface
from helpers.requestFacade import requestFacade

# Initialise class
class Merriam(WordInterface):
    # Initialise constructor
    def __init__(self):
        # Initialise baseURL
        self.baseURL = "https://www.merriam-webster.com"
        # Initialise sender
        self.sender = requestFacade()
        # Initialise default word
        self.word = {
            "word": "whilom",
            "wordType": "adverb",
            "pronunciation": "whi-lom"
        }

    # Initialise function to get word
    def getWord(self):
        """Send request to merriam webster site and scrape for 'word of the day'"""
        # Define word object
        word = {}
        # Prepare URL
        URL = os.path.join(self.baseURL, "word-of-the-day")
        # Call function to send request and get HTML response
        res = self.sender["HTML"](URL)
        # Check status code
        if res["status"] == 200:
            # Extract word
            word["word"] = res["payload"].select(".word-and-pronunciation h1")[0].text
            # Extract data about word
            temp = res["payload"].select(".word-attributes")[0]
            word["wordType"] = temp.select(".main-attr")[0].text
            word["pronunciation"] = temp.select(".word-syllables")[0].text
            # Replace default word
            self.word = word
        # Return word object
        return self.word
