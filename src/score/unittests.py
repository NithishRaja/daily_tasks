#
# File containing unit tests for quote class
#
#

# Dependencies
import unittest
# Local Dependencies
from scoreGetter import ScoreGetter

class TestScoreGetterMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise score getter object
        self.scoreGetterObj = ScoreGetter()
    # Check today score
    def test_get_score_today(self):
        # Call function
        res = self.scoreGetterObj.getScoreByDay(self.scoreGetterObj.getCurrentDate())
        # Check if response is an array
        self.assertIs(type(res), type([]))
        # Check size of array
        self.assertTrue(len(res) >= 0)
    # Check get score by day for successful request
    def test_get_score_by_day_for_successful_response(self):
        gameAttrList = ["gameId", "boxscoreURL", "title", "subtitle", "clock", "hTeam", "vTeam"]
        # Call function
        res = self.scoreGetterObj.getScoreByDay("20210720")
        # Check if response is an array
        self.assertIs(type(res), type([]))
        # Check size of array
        self.assertTrue(len(res) == 1)
        # Check game attributes
        for item in gameAttrList:
            self.assertTrue(item in res[0].keys())
    # Check get score by day for day with no games
    def test_get_score_by_day_for_no_games(self):
        # Call function
        res = self.scoreGetterObj.getScoreByDay("20210721")
        # Check if response is an array
        self.assertIs(type(res), type([]))
        # Check size of array
        self.assertTrue(len(res) == 0)
    # Check get score by day for failed request
    def test_get_score_by_day_for_failed_response(self):
        # Update link
        self.scoreGetterObj.links["links"]["scoreboard"] = "https://the-internet.herokuapp.com/status_codes/404"
        # Call function
        res = self.scoreGetterObj.getScoreByDay("20210720")
        # Check if response is an array
        self.assertIs(type(res), type([]))
        # Check size of array
        self.assertTrue(len(res) == 0)
    # Check for score with empty links list
    def test_get_score_by_day_with_empty_links(self):
        # Update link
        self.scoreGetterObj.links = {}
        # Call function
        res = self.scoreGetterObj.getScoreByDay("20210720")
        # Check if response is an array
        self.assertIs(type(res), type([]))
        # Check size of array
        self.assertTrue(len(res) == 0)
    # Tear down function
    def tearDown(self):
        del self.scoreGetterObj

if __name__ == "__main__":
    unittest.main()
