#
# File containing unit tests for quote class
#
#

# Dependencies
import unittest, requests, sys, os

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from helpers.requestFacade import requestFacade
from quoteGetter import QuoteGetter

def simulate_failed_response(url):
    res = requests.get("https://the-internet.herokuapp.com/status_codes/404")
    return {
        "status": res.status_code,
        "payload": res.text
    }

def simulationFacade():
    return {
        "HTML": simulate_failed_response,
        "JSON": simulate_failed_response
    }

class TestQuoteGetterMethods(unittest.TestCase):
    def setUp(self):
        self.quoteGetterObj = QuoteGetter(requestFacade())

    def test_random_quote_normal_response(self):
        randomQuote = self.quoteGetterObj.getRandomQuote()
        self.assertTrue("author", randomQuote)
        self.assertTrue("text", randomQuote)

    def test_random_quote_failed_response(self):
        self.quoteGetterObj.sender = simulationFacade()
        randomQuote = self.quoteGetterObj.getRandomQuote()
        self.assertTrue("topic" in randomQuote)
        self.assertTrue("author" in randomQuote)
        self.assertTrue("text" in randomQuote)
        self.assertEqual(randomQuote["topic"], "welp!")
        self.assertEqual(randomQuote["author"], "cocoa puffs")
        self.assertEqual(randomQuote["text"], "to refactor or to start from scratch?")

    def tearDown(self):
        del self.quoteGetterObj

if __name__ == "__main__":
    unittest.main()
