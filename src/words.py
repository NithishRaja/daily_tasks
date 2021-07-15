#
# File containing class to get words of the day
#
#

# Dependencies
import os
# Local Dependencies
from getter import Getter
from helpers.requestFactory import requestFactory

class Words(Getter):
    # Define constructor
    def __init__(self):
        # Initialise URLs
        self.merriam_webster_url = "https://www.merriam-webster.com"
        self.dictionary_url = "https://www.dictionary.com"
        # Initialise sender
        self.sender = requestFactory()

    # Function to get word from merriam webster
    def getMerriamWebsterWord(self):
        """Send request to merriam webster site and scrape for 'word of the day'"""
        # Define word object
        word = None
        # Prepare URL
        URL = os.path.join(self.merriam_webster_url, "word-of-the-day")
        # Call function to send request and get HTML response
        res = self.sender["HTML"](URL)
        # Check status code
        if res["status"] == 200:
            # Initialise word object
            word = {}
            # Extract word
            word["word"] = res["payload"].select(".word-and-pronunciation h1")[0].text
            # Extract data about word
            temp = res["payload"].select(".word-attributes")[0]
            word["wordType"] = temp.select(".main-attr")[0].text
            word["pronunciation"] = temp.select(".word-syllables")[0].text
        # Return word object
        return word

    # Function to get word from dictionary
    def getDictionaryWord(self):
        """Send request to dictionary site and scrape for 'word of the day'"""
        # Define word object
        word = None
        # Prepare URL
        URL = os.path.join(self.dictionary_url, "e", "word-of-the-day")
        # Call function to send request and get HTML response
        res = self.sender["HTML"](URL)
        # Check status code
        if res["status"] == 200:
            # Initialise word object
            word = {}
            # Extract word
            temp = res["payload"].select(".otd-item-headword")[0]
            word["word"] = temp.select(".otd-item-headword__word h1")[0].text
            # Extract data about word
            word["wordType"] = temp.select(".otd-item-headword__pos p")[0].text.replace("\n", "").replace(" ", "")
            pronunciation = temp.select(".otd-item-headword__pronunciation")[0].text
            word["pronunciation"] = pronunciation.replace("\n", "").replace(" ", "").replace("[", "").replace("]", "")
        # Return word object
        return word

    def getMeaning(self, word):
        """Send request to merriam webster site and scrape for meaning of given word.

        Keyword Arguments:
        word -- string
        """
        # Initialise array to hold results
        data = []
        # Prepare URL
        URL = os.path.join(self.merriam_webster_url, "dictionary", word)
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

    def getData(self):
        """Function to call functions to get 'words of the day' and their meanings."""
        # Initialise array to hold words
        data = []
        # Call function to get word from merriam webster
        word = self.getMerriamWebsterWord()
        # Check if word is not None
        if not word == None:
            # Call function to get meaning
            word["meaning"] = self.getMeaning(word["word"])
            # Append word to list
            data.append(word)
        # Call function to get word from dictionary
        word = self.getDictionaryWord()
        # Check if word is not None
        if not word == None:
            # Call function to get meaning of word
            word["meaning"] = self.getMeaning(word["word"])
            # Append word to list
            data.append(word)
        # Return list of words
        return data
