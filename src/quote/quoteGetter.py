#
# File containing class to get Quote
#
#

# Dependencies
import os, random

# Local Dependencies
from compose.quoteGetterInterface import QuoteGetterInterface

# Initialise class
class QuoteGetter(QuoteGetterInterface):
    # Initialise constructor
    def __init__(self, sender):
        # Set baseURL
        self.baseURL = "http://api.quotable.io"
        # Initialise list for topic index
        self.topicIndex = []
        # Initialise list for topic index
        self.topicList = []
        # Initialise sender
        self.sender = sender

    def getRandomQuote(self):
        """Function to call API and get random quote"""
        quoteObj = {
            "topic": "welp!",
            "author": "cocoa puffs",
            "text": "to refactor or to start from scratch?"
        }
        res = self.sender["JSON"](os.path.join(self.baseURL, "random"))
        if res["status"] == 200:
            quoteObj["topic"] = res["payload"]["tags"][0]
            quoteObj["author"] = res["payload"]["author"]
            quoteObj["text"] = res["payload"]["content"]

        return quoteObj
