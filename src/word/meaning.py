#
# File containing code to get meaning of word
#
#

# Dependencies
import os

# Local Dependencies
from meaningInterface import MeaningInterface

# Initialise class
class Meaning(MeaningInterface):
    # Initialise constructor
    def __init__(self, sender):
        # Initialise baseURL
        self.baseURL = "https://www.merriam-webster.com"
        # Initialise sender
        self.sender = sender

    # Function to get meaning of word
    def getMeaning(self, word):
        """Scrape HTML for meaning of given word.

        Keyword Arguments:
        word -- string
        """
        # Initialise array to hold results
        data = []
        # Prepare URL
        URL = os.path.join(self.baseURL, "dictionary", word)
        # Call function to send request and get HTML response
        res = self.sender["HTML"](URL)
        # Check status code
        if res["status"] == 200:
            # Get text
            meaningList = res["payload"].select("#dictionary-entry-1 .dtText")
            # Append meaning to array
            for item in meaningList:
                data.append(item.text)
        # Return list of meanings
        return data
