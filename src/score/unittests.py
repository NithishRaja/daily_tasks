#
# File containing unit tests for quote class
#
#

# Dependencies
import unittest
# Local Dependencies
from score import Score

class TestScoreMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise quote object
        self.scoreObj = Score()
    # Check today score
    def test_get_score_today(self):
        # Call function
        res = self.scoreObj.getScoreToday()
        # Check if response is an array
        self.assertIs(type(res), type([]))
        # Check size of array
        self.assertTrue(len(res) >= 0)
    # Check get score by day for successful request
    def test_get_score_by_day_for_successful_response(self):
        gameAttrList = ["gameId", "boxscoreURL", "title", "subtitle", "clock", "hTeam", "vTeam"]
        # Call function
        res = self.scoreObj.getScoreByDay("20210720")
        # Check if response is an array
        self.assertIs(type(res), type([]))
        # Check size of array
        self.assertTrue(len(res) == 1)
        # Check game attributes
        for item in gameAttrList:
            self.assertTrue(item in res[0].keys())
    # Check get score by day for failed request
    def test_get_score_by_day_for_failed_response(self):
        # Initialise score object
        scoreObj = Score()
        # Update link
        scoreObj.links["links"]["scoreboard"] = "https://the-internet.herokuapp.com/status_codes/404"
        # Call function
        res = scoreObj.getScoreByDay("20210720")
        # Check if response is an array
        self.assertIs(type(res), type([]))
        # Check size of array
        self.assertTrue(len(res) == 0)
    # Check for score with empty links list
    def test_get_score_by_day_with_empty_links(self):
        # Initialise score object
        scoreObj = Score()
        # Update link
        scoreObj.links = {}
        # Call function
        res = scoreObj.getScoreByDay("20210720")
        # Check if response is an array
        self.assertIs(type(res), type([]))
        # Check size of array
        self.assertTrue(len(res) == 0)
    # Tear down function
    def tearDown(self):
        del self.scoreObj

if __name__ == "__main__":
    unittest.main()
