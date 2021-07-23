#
# File containing class for getting word from dictionary.com
#
#

# Dependencies
import os

# Local Dependencies
from wordInterface import WordInterface

# Initialise class
class Dictionary(WordInterface):
    # Initialise constructor
    def __init__(self, sender):
        # Initialise baseURL
        self.baseURL = "https://www.dictionary.com"
        # Initialise sender
        self.sender = sender
        # Initialise default word
        self.word = {
            "word": "altruism",
            "wordType": "noun",
            "pronunciation": "al-troo-iz-uhm"
        }

    # Initialise function to get word
    def getWord(self):
        """Send request to dictionary site and scrape for 'word of the day'"""
        # Define word object
        word = {}
        # Prepare URL
        URL = os.path.join(self.baseURL, "e", "word-of-the-day")
        # Call function to send request and get HTML response
        res = self.sender["HTML"](URL)
        # Check status code
        if res["status"] == 200:
            # Extract word
            temp = res["payload"].select(".otd-item-headword")[0]
            word["word"] = temp.select(".otd-item-headword__word h1")[0].text
            # Extract data about word
            word["wordType"] = temp.select(".otd-item-headword__pos p")[0].text.replace("\n", "").replace(" ", "")
            pronunciation = temp.select(".otd-item-headword__pronunciation")[0].text
            word["pronunciation"] = pronunciation.replace("\n", "").replace(" ", "").replace("[", "").replace("]", "")
            # Replace default word with current word
            self.word = word
        # Return word object
        return self.word
