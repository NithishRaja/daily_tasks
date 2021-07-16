#
# File containing unit tests for quote class
#
#

# Dependencies
import unittest
# Local Dependencies
from quote import Quote

class TestQuoteMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise quote object
        self.quoteObj = Quote()
    # Check output of quote topic index for successful request
    def test_quote_topic_index_normal_response(self):
        res = self.quoteObj.getTopicIndex()
        self.assertTrue(len(res) == 226)
    # Check output of quote topic index for failed request
    def test_quote_topic_index_failed_response(self):
        quoteObj = Quote()
        quoteObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        res = quoteObj.getTopicIndex()
        self.assertIs(type(res), type([]))
        self.assertTrue(len(res) == 0)
    # Check output of quote topic index for successful request
    def test_quote_topic_normal_response(self):
        indexURL = "/topic_index/ec"
        res = self.quoteObj.getTopicList(indexURL)
        self.assertTrue(len(res) == 64)
    # Check output of quote topic index for failed request
    def test_quote_topic_failed_response(self):
        quoteObj = Quote()
        quoteObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        indexURL = ""
        res = quoteObj.getTopicList(indexURL)
        self.assertIs(type(res), type([]))
        self.assertTrue(len(res) == 0)
    # Check quote by URL for normal response
    def test_quote_data_by_URL_normal_response(self):
        topicURL = "/topics/echoes-quotes"
        res = self.quoteObj.getQuoteDataByURL(topicURL)
        self.assertTrue(len(res) >= 45)
    def test_quote_data_by_URL_failed_response(self):
        quoteObj = Quote()
        quoteObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        topicURL = ""
        res = quoteObj.getQuoteDataByURL(topicURL)
        self.assertIs(type(res), type([]))
        self.assertTrue(len(res) == 0)
    # Check quote by topic for normal response
    def test_quote_data_by_topic_normal_response(self):
        topic = "Echoes"
        res = self.quoteObj.getQuoteDataByTopic(topic)
        self.assertTrue(len(res) >= 45)
    # Check quote by topic for failed response
    def test_quote_data_by_topic_failed_response(self):
        quoteObj = Quote()
        quoteObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        topicURL = ""
        res = quoteObj.getQuoteDataByURL(topicURL)
        self.assertIs(type(res), type([]))
        self.assertTrue(len(res) == 0)
    # Tear down function
    def tearDown(self):
        del self.quoteObj

if __name__ == "__main__":
    unittest.main()
