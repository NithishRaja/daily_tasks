#
# File containing unit tests for quote class
#
#

# Dependencies
import unittest
# Local Dependencies
from quoteGetter import QuoteGetter

class TestQuoteMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise quote object
        self.quoteGetterObj = QuoteGetter()
    # Check output of quote topic index for successful request
    def test_quote_topic_index_normal_response(self):
        res = self.quoteGetterObj.getTopicIndex()
        self.assertTrue(len(res) == 226)
    # Check output of quote topic index for failed request
    def test_quote_topic_index_failed_response(self):
        self.quoteGetterObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        res = self.quoteGetterObj.getTopicIndex()
        self.assertIs(type(res), type([]))
        self.assertTrue(len(res) == 0)
    # Check output of quote topic index for successful request
    def test_quote_topic_normal_response(self):
        indexURL = "/topic_index/ec"
        res = self.quoteGetterObj.getTopicList(indexURL)
        self.assertTrue(len(res) == 64)
    # Check output of quote topic index for failed request
    def test_quote_topic_failed_response(self):
        self.quoteGetterObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        indexURL = ""
        res = self.quoteGetterObj.getTopicList(indexURL)
        self.assertIs(type(res), type([]))
        self.assertTrue(len(res) == 0)
    # Check quote by URL for normal response
    def test_quote_data_by_URL_normal_response(self):
        topicURL = "/topics/echoes-quotes"
        res = self.quoteGetterObj.getQuoteDataByURL(topicURL)
        self.assertTrue(len(res) >= 45)
    def test_quote_data_by_URL_failed_response(self):
        self.quoteGetterObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        topicURL = ""
        res = self.quoteGetterObj.getQuoteDataByURL(topicURL)
        self.assertIs(type(res), type([]))
        self.assertTrue(len(res) == 0)
    # Check quote by topic for normal response
    def test_quote_data_by_topic_normal_response(self):
        topic = "Echoes"
        res = self.quoteGetterObj.getQuoteDataByTopic(topic)
        self.assertTrue(len(res) >= 45)
    # Check quote by topic for failed response
    def test_quote_data_by_topic_failed_response(self):
        self.quoteGetterObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        topicURL = ""
        res = self.quoteGetterObj.getQuoteDataByURL(topicURL)
        self.assertIs(type(res), type([]))
        self.assertTrue(len(res) == 0)
    # Tear down function
    def tearDown(self):
        del self.quoteGetterObj

if __name__ == "__main__":
    unittest.main()
