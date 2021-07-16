#
# File containing class to get Quote
#
#

# Dependencies
import os, sys

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from helpers.requestFactory import requestFactory

# Initialise class
class Quote:
    # Initialise constructor
    def __init__(self):
        # Set baseURL
        self.baseURL = "https://www.brainyquote.com"
        # Initialise sender
        self.sender = requestFactory()

    # Function to get quote topics index
    def getTopicIndex(self):
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
        # Return list
        return topicIndex

    # Function to get list of quote topics
    def getTopicList(self, indexURL):
        """Function to scrape baseURL+indexURL for selected quote topics.

        Keyword Arguments:
        indexURL -- string
        """
        # Initialise array to hold topics
        topics = []
        # Prepare URL
        URL = self.baseURL + indexURL
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
        return topics

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

    # Function to get quote data
    def getQuoteDataByTopic(self, topic):
        """Function to prepeare URL for given topic and call getQuoteDataByURL.

        Keyword Arguments:
        topic -- string
        """
        # Generate quote URL
        topicURL = "/topics/"+topic.lower()+"-quotes"
        # Call function to get list of quotes
        quotes = self.getQuoteDataByURL(topicURL)
        # Return list
        return quotes

if __name__ == "__main__":
    obj = Quote()
    index = obj.getTopicIndex()
    print(index[0])
    print(len(index))
