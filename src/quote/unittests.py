#
# File containing unit tests for quote class
#
#

# Dependencies
import unittest
# Local Dependencies
from quoteGetter import QuoteGetter

class TestQuoteGetterMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise quote object
        self.quoteGetterObj = QuoteGetter()
    # Check output of quote topic index for successful request
    def test_quote_topic_index_normal_response(self):
        # Check topic index type
        self.assertIs(type(self.quoteGetterObj.topicIndex), type([]))
        # Check topic index length
        self.assertEqual(len(self.quoteGetterObj.topicIndex), 226)
    # Check output of quote topic index for failed request
    def test_quote_topic_index_failed_response(self):
        self.quoteGetterObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        # Call function to populate topic index
        self.quoteGetterObj.populateTopicIndex()
        # Check topic index type
        self.assertIs(type(self.quoteGetterObj.topicIndex), type([]))
        # Check topic index length
        self.assertEqual(len(self.quoteGetterObj.topicIndex), 0)
    # Check quote topic list for successful request
    def test_quote_topic_normal_response(self):
        self.quoteGetterObj.selectedTopicIndex = {
            "name": "test",
            "href": "/topic_index/ec"
        }
        # Call function to populate topic list
        self.quoteGetterObj.populateTopicList()
        # Check type
        self.assertIs(type(self.quoteGetterObj.topicList), type([]))
        # Check length
        self.assertEqual(len(self.quoteGetterObj.topicList), 64)
    # Check output of quote topic index for failed request
    def test_quote_topic_failed_response(self):
        self.quoteGetterObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        self.selectedTopicIndex = {
            "name": "test",
            "href": "/topic_index/ec"
        }
        # Call function to populate topic list
        self.quoteGetterObj.populateTopicList()
        # Check type
        self.assertIs(type(self.quoteGetterObj.topicList), type([]))
        # Check length
        self.assertEqual(len(self.quoteGetterObj.topicList), 0)
    # Check quote by URL for normal response
    def test_quote_data_by_URL_normal_response(self):
        topicURL = "/topics/echoes-quotes"
        res = self.quoteGetterObj.getQuoteDataByURL(topicURL)
        # Check type
        self.assertIs(type(res), type([]))
        # Check length
        self.assertTrue(len(res) >= 45)
        # Check attributes
        for item in ["text", "author"]:
            self.assertTrue(item in res[0].keys())
    def test_quote_data_by_URL_failed_response(self):
        self.quoteGetterObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        topicURL = ""
        res = self.quoteGetterObj.getQuoteDataByURL(topicURL)
        # Check type
        self.assertIs(type(res), type([]))
        # Check length
        self.assertEqual(len(res), 0)
    def test_getQuoteList_normal_response(self):
        res = self.quoteGetterObj.getQuoteList()
        # Check type of response
        self.assertIs(type(res), type({}))
        # Check attributes
        for item in ["topic", "quotes"]:
            self.assertTrue(item in res.keys())
        # Check type of res["quotes"]
        self.assertIs(type(res["quotes"]), type([]))
        # Check attributes
        for item in ["text", "author"]:
            self.assertTrue(item in res["quotes"][0].keys())
    def test_getQuoteList_failed_response(self):
        # Initialise default quote
        defaultQuote = {
            "text": "To refactor or to start from scratch?",
            "author": "Cocoa Puffs"
        }
        self.quoteGetterObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        res = self.quoteGetterObj.getQuoteList()
        # Check type of response
        self.assertIs(type(res), type({}))
        # Check length of res["quotes"]
        self.assertEqual(len(res["quotes"]), 1)
        # Check attributes
        for item in ["text", "author"]:
            self.assertEqual(res["quotes"][0][item], defaultQuote[item])
    # Tear down function
    def tearDown(self):
        del self.quoteGetterObj

if __name__ == "__main__":
    unittest.main()
