#
# File containing class to get Quote
#
#

# Dependencies
import os, sys, random

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from helpers.requestFacade import requestFacade
from quoteGetterInterface import QuoteGetterInterface

# Initialise class
class QuoteGetter(QuoteGetterInterface):
    # Initialise constructor
    def __init__(self):
        # Set baseURL
        self.baseURL = "https://www.brainyquote.com"
        # Initialise list for topic index
        self.topicIndex = []
        # Initialise list for topic index
        self.topicList = []
        # Initialise sender
        self.sender = requestFacade()

        # Call function to get topic index
        self.populateTopicIndex()
        # Initialise variable for selected topic index
        self.selectedTopicIndex = self.randomSelectElement(self.topicIndex)

        # Call function to get topic list
        self.populateTopicList()


    # Function to get quote topics index
    def populateTopicIndex(self):
        """Function to scrape baseURL for compressed quote topics list"""
        # Initialise array for index
        topicIndex = []
        # Send request
        res = self.sender["HTML"](os.path.join(self.baseURL, "topics"))
        # Check response status
        if res["status"] == 200:
            # Get compressed list of topics
            temp = res["payload"].select(".bq_s .bq_fl .bqLn a")
            # Extract name and href
            for item in temp:
                topicIndex.append({
                    "name": item.text,
                    "href": item["href"]
                })
        # Set topic index
        self.topicIndex = topicIndex

    # Function to select a random element from list
    def randomSelectElement(self, list):
        """Randomly select an item from given list and return it.

        Keyword Arguments:
        list -- array
        """
        return random.choice(list)


    # Function to get list of quote topics
    def populateTopicList(self):
        """Function to scrape for list of quote topics."""
        # Initialise array to hold topics
        topics = []
        # Prepare URL
        URL = self.baseURL + self.selectedTopicIndex["href"]
        # Send request
        res = self.sender["HTML"](URL)
        # Check response status
        if res["status"] == 200:
            # Get list of topics
            temp = res["payload"].select(".bqLn a")
            # Extract name and href
            for item in temp:
                topics.append({
                    "name": item.text,
                    "href": item["href"]
                })
        # Return list
        self.topicList = topics

    # Function to get quote data
    def getQuoteDataByURL(self, topicURL):
        """Function to scrape baseURL+topicURL for quotes.

        Keyword Arguments:
        topicURL -- string
        """
        # Initialise array to hold quote data
        quotes = []
        # Prepare URL
        URL = self.baseURL + topicURL
        # Send request
        res = self.sender["HTML"](URL)
        # Check response status
        if res["status"] == 200:
            # Get list of topics
            temp = res["payload"].select(".bqLn a")
            # Get quote list
            quoteList = res["payload"].select("#quotesList .bqQt")
            # Iterate over all quotes
            for item in quoteList:
                # Append quote data to list
                quotes.append({
                    "text": item.find("a", {"title": "view quote"}).text,
                    "author": item.find("a", {"title": "view author"}).text
                })
        # Return quote list
        return quotes

    # Function to get quotes from a randomly selected topic
    def getQuoteList(self):
        # Call function to select a topic at random
        selectedTopic = self.randomSelectElement(self.topicList)
        # Call function to get quote list
        quoteList = self.getQuoteDataByURL(selectedTopic["href"])
        # Check if quote list is empty
        if len(quoteList) == 0:
            quoteList.append({
                "text": "To refactor or to start from scratch?",
                "author": "Cocoa Puffs"
            })
        # Return data
        return {
            "topic": selectedTopic["name"],
            "quotes": quoteList
        }
