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
        self.selectedTopic = ""
        # Initialise array to hold quote list
        self.quoteList = []
        # Initialise default quote
        self.defaultQuote = {
            "text": "To refactor or to start from scratch?",
            "author": "Cocoa Puffs"
        }

        # Call function to fill topic index
        self.populateTopicIndexList()
        # Call function to fill topic list
        self.populateTopicList()
        # Call function to fill quote list
        self.populateQuoteList()

    # Function to get topic index list
    def populateTopicIndexList(self):
        """Calls Quote.getTopicIndex and stores it."""
        # Call function to get topic index
        self.topicIndexList = self.quote.getTopicIndex()

    # Function to get topic list
    def populateTopicList(self):
        """Selects a random topic index and stores it."""
        # Check length of topic index list
        if not len(self.topicIndexList) == 0:
            # Select random topic index
            temp = self.topicIndexList[ random.randint(0, len(self.topicIndexList)-1) ]
            # Call function to get topic list
            self.topicList = self.quote.getTopicList( temp["href"] )

    # Function to get quote list
    def populateQuoteList(self):
        """Gets a list of quotes for a randomly selected topic."""
        # Select a random topic
        temp = self.topicList[ random.randint(0, len(self.topicList)-1) ]
        # Set selected topic
        self.selectedTopic = temp["name"]
        # Call function to get topic list
        self.quoteList = self.quote.getQuoteDataByURL( temp["href"] )

    # Function to get a random quote
    def getData(self):
        """Selects a random quote from list."""
        # Initialise variable for quote
        quote = self.defaultQuote
        # Check if quote list is empty
        if not len(self.quoteList) == 0:
            # Get a random quote
            quote = self.quoteList[ random.randint(0, len(self.quoteList)-1) ]
        # Add topic to quote
        quote["topic"] = self.selectedTopic
        # Return selected quote
        return quote
