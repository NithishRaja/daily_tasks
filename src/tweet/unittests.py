#
# File containing unit tests for tweet components
#
#

# Dependencies
import unittest, requests, sys, os, json

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from helpers.requestFacade import requestFacade
from tweetGetter import TweetGetter

def simulate_failed_response(url, headers={}):
    res = requests.get("https://the-internet.herokuapp.com/status_codes/404")
    return {
        "status": res.status_code,
        "payload": res.text
    }

def simulationFacade():
    return {
        "JSON": simulate_failed_response
    }

# Read config
file = open(os.path.join("credentials.json"))
credentials = json.load(file)
file.close()

class TestTweetGetterMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        self.tweetGetterObj = TweetGetter(requestFacade())
        self.tweetGetterObj.addToken(credentials["twitter"]["BearerToken"])
    # Check getTweetList normal request
    def test_getTweetList_normal_response(self):
        # Initialise variable for count
        count = 3
        res = self.tweetGetterObj.getTweetList("NBA")
        # Check response type
        self.assertIs(type(res), type([]))
        # Check response length
        self.assertEqual(len(res), count)
        # Check attributes
        for item in ["text", "name", "username", "profile_image_url", "id"]:
            for currentItem in range(count):
                    self.assertTrue(item in res[currentItem].keys())
    # Check getTweetList failed request
    def test_getTweetList_failed_response(self):
        self.tweetGetterObj.sender = simulationFacade()
        res = self.tweetGetterObj.getTweetList("NBA")
        # Check response type
        self.assertIs(type(res), type([]))
        # Check response length
        self.assertEqual(len(res), 0)
    # Check getTweetList for bad request
    def test_getTweetList_bad_response(self):
        res = self.tweetGetterObj.getTweetList("igdfgfl fjgfuigefig fugwefuiegwfugiwe afdf")
        # Check response type
        self.assertIs(type(res), type([]))
        # Check response length
        self.assertEqual(len(res), 0)
    # Tear down function
    def tearDown(self):
        del self.tweetGetterObj

if __name__ == "__main__":
    unittest.main()
