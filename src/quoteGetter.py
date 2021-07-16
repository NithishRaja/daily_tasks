#
# File to get a random quote
#
#

# Dependencies
import random
# Local Dependencies
from getter import Getter
from quote.quote import Quote

class QuoteGetter(Getter):
    def __init__(self):
        # Initialise quote object
        self.quote = Quote()
        # Initialise array to hold topic index
        self.topicIndexList = []
        # Initialise array to hold topic list
        self.topicList = []
        # Initialise variable to hold selected topic
        self.selectedTopic = "One of Many"
        # Initialise array to hold quote list
        self.quoteList = [{
            "text": "To refactor or to start from scratch?",
            "Author": "Cocoa Puffs"
        }]
        # Initialise variables for retries
        self.maxRetries = 3
        self.retryCount = 0
        # Call function to fill topic index
        self.populateTopicIndexList()
        # Call function to fill topic list
        self.populateTopicList()
        # Call function to fill quote list
        self.populateQuoteList()

    # Function to get topic index list
    def populateTopicIndexList(self):
        """Calls Quote.getTopicIndex and stores it, retries upon empty list."""
        # Iterate upon failure
        while self.retryCount < self.maxRetries:
            # Call function to get topic index
            self.topicIndexList = self.quote.getTopicIndex()
            # Check length of list
            if len(self.topicIndexList) > 0:
                break
            else:
                # Increment retry count upon failure
                self.retryCount = self.retryCount + 1

    # Function to get topic list
    def populateTopicList(self):
        """Selects a random topic index and stores it, retries upon empty list."""
        # Check length of topic index list
        if not len(self.topicIndexList) == 0:
            # Iterate upon failure
            while self.retryCount < self.maxRetries:
                # Select random topic index
                temp = self.topicIndexList[ random.randint(0, len(self.topicIndexList)-1) ]
                # Call function to get topic list
                self.topicList = self.quote.getTopicList( temp["href"] )
                # Check length of list
                if len(self.topicList) > 0:
                    break
                else:
                    # Increment retry count upon failure
                    self.retryCount = self.retryCount + 1

    # Function to get quote list
    def populateQuoteList(self):
        """Gets a list of quotes for a randomly selected topic."""
        # Check length of topic index list
        if not len(self.topicList) == 0:
            # Iterate upon failure
            while self.retryCount < self.maxRetries:
                # Select a random topic
                temp = self.topicList[ random.randint(0, len(self.topicList)-1) ]
                self.selectedTopic = temp["name"]
                # Call function to get topic list
                res = self.quote.getQuoteDataByURL( temp["href"] )
                # Check length of list
                if len(res) > 0:
                    self.quoteList = res
                    break
                else:
                    # Increment retry count upon failure
                    self.retryCount = self.retryCount + 1

    # Function to get a random quote
    def getData(self):
        """Selects a random quote from list."""
        # Get a random quote
        temp = self.quoteList[ random.randint(0, len(self.quoteList)-1) ]
        # Add topic to quote
        temp["topic"] = self.selectedTopic
        # Return selected quote
        return temp
