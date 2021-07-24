#
# File containing unit tests
#
#

# Dependencies
import unittest, requests, sys, os

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from helpers.requestFacade import requestFacade
from dayGetter import DayGetter

def simulate_failed_response(url):
    res = requests.get("https://the-internet.herokuapp.com/status_codes/404")
    return {
        "status": res.status_code,
        "payload": res.text
    }

def simulationFacade():
    return {
        "HTML": simulate_failed_response
    }

class TestDayGetterMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise day object
        self.dayGetterObj = DayGetter(requestFacade())
    # Check output of getDayByDate function for normal specified request
    def test_day_getter_specified_date(self):
        # Initialise array to hold titles
        titleList = ["French Fries Day", "Cow Appreciation Day", "Beef Tallow Day", "International Rock Day", "Embrace Your Geekness Day"]
        # Call function to get data by date
        res = self.dayGetterObj.getDayByDate(day=13, month=7)
        # Check length of array
        self.assertEqual(len(res), len(titleList))
        # Check elements of array
        for item in res:
            self.assertTrue(item["text"] in titleList)
    # Check output of getDayByDate function for bad request
    def test_day_getter_empty_response(self):
        # Call function to get data
        dayList = self.dayGetterObj.getDayByDate(day=-13, month=-7)
        # Check length of array
        self.assertEqual(len(dayList), 0)
    # Check output of getDayByDate function for failed request
    def test_day_getter_failed_response(self):
        self.dayGetterObj.sender = simulationFacade()
        # Call function to get data
        dayList = self.dayGetterObj.getDayByDate(day=-13, month=-7)
        # Check length of array
        self.assertEqual(len(dayList), 0)
    # Tear down function
    def tearDown(self):
        del self.dayGetterObj

if __name__ == "__main__":
    unittest.main()
