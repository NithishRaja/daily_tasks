#
# File containing unit tests
#
#

# Dependencies
import unittest, json
# Local Dependencies
from dayGetter import DayGetter
from quoteGetter import QuoteGetter
from eventGetter import EventGetter
from scoreGetter import ScoreGetter

# Read in credentials
file = open("./credentials.json")
credentials = json.load(file)
file.close()

# Read in credentials
file = open("./config.json")
config = json.load(file)
file.close()

class TestDayGetterMethods(unittest.TestCase):
    # Set up fuction
    def setUp(self):
        self.dayGetterObj = DayGetter()
    # Check day getter getData
    def test_dey_getter_getData(self):
        self.assertIs(type(self.dayGetterObj.getData()), type([]))
    # Tear down function
    def tearDown(self):
        del self.dayGetterObj

class TestQuoteGetterMethods(unittest.TestCase):
    # Set up fuction
    def setUp(self):
        self.quoteGetterObj = QuoteGetter()
    # Check quote getter for successful request
    def test_quote_getter_getData_on_success(self):
        # Initialise list of fileds in quote data
        quoteFields = ["text", "topic", "author"]
        # Call function to get quote data
        res = self.quoteGetterObj.getData()
        # Check response type
        self.assertIs(type(res), type({}))
        # Check fields of object
        for item in res.keys():
            self.assertTrue(item in quoteFields)
    # Check quote getter for failed request
    def test_quote_getter_getData_on_failure(self):
        # Initialise default quote object
        defaultQuote = {
            "text": "To refactor or to start from scratch?",
            "author": "Cocoa Puffs",
        }
        # Initialise quoteGetter object
        quoteGetterObj = QuoteGetter()
        quoteGetterObj.quoteList = []
        # Call function to get quote data
        res = quoteGetterObj.getData()
        # Check response
        for item in defaultQuote.keys():
            self.assertEqual(res[item], defaultQuote[item])
    # Tear down function
    def tearDown(self):
        del self.quoteGetterObj

class TestEventGetterMethods(unittest.TestCase):
    # Set up fuction
    def setUp(self):
        self.eventGetterObj = EventGetter()
    # Check get data
    def test_event_getter_getData(self):
        # Check response
        self.assertEqual(type(self.eventGetterObj.getData()), type([]))
    # Tear down function
    def tearDown(self):
        del self.eventGetterObj

class TestScoreGetterMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise object
        self.scoreGetterObj = ScoreGetter()
    # Check get data
    def test_score_geter_getData(self):
        # Initialise attribute list
        attributeList = ["currentDate", "standingsURL", "games"]
        # Get data
        res = self.scoreGetterObj.getData()
        # Check attributes
        for item in attributeList:
            self.assertTrue(item in res.keys())
    # Tear down function
    def tearDown(self):
        del self.scoreGetterObj

if __name__ == '__main__':
    unittest.main()
