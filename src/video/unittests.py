#
# File containing unit tests for song and lyric components
#
#

# Dependencies
import unittest, requests, json, sys, os

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from helpers.requestFacade import requestFacade
from videoGetter import VideoGetter

def simulate_failed_response(url):
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

class TestSongGetterMethods(unittest.TestCase):
    # Set up fuction
    def setUp(self):
        self.videoGetterObj = VideoGetter(requestFacade())
        self.videoGetterObj.addKey(credentials["youtube"]["APIKey"])
    # Test get video for successful request
    def test_getVideo_for_successful_response(self):
        res = self.videoGetterObj.getVideoURL("some video")
        # Check response type
        self.assertIs(type(res), type(""))
    # Test get video for failed request
    def test_getVideo_for_failed_response(self):
        self.videoGetterObj.sender = simulationFacade()
        res = self.videoGetterObj.getVideoURL("")
        # Check response type
        self.assertIs(type(res), type(None))
    # Test get video for bad request
    def test_getVideo_for_empty_response(self):
        res = self.videoGetterObj.getVideoURL("oilvasfpvpfvepifevfifvispdvfuipfvfvfvfv")
        # Check response type
        self.assertIs(type(res), type(None))
    # Tear down function
    def tearDown(self):
        del self.videoGetterObj

if __name__ == "__main__":
    unittest.main()
