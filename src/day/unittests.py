#
# File containing unit tests
#
#

# Dependencies
import unittest
# Local Dependencies
from day import Day
from dayGetter import DayGetter

class TestDayMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise day object
        self.dayObj = Day()
    # Check output of getDayByDate function for normal specified request
    def test_day_specified_date(self):
        # Initialise array to hold titles
        titleList = ["French Fries Day", "Cow Appreciation Day", "Beef Tallow Day", "International Rock Day", "Embrace Your Geekness Day"]
        # Call function to get data by date
        res = self.dayObj.getDayByDate(day=13, month=7)
        # Check length of array
        self.assertEqual(len(res), len(titleList))
        # Check elements of array
        for item in res:
            self.assertTrue(item["text"] in titleList)
    # Check output of getDayByDate function for bad request
    def test_day_empty_response(self):
        # Call function to get data
        dayList = self.dayObj.getDayByDate(day=-13, month=-7)
        # Check length of array
        self.assertEqual(len(dayList), 0)
    # Tear down function
    def tearDown(self):
        del self.dayObj

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

if __name__ == "__main__":
    unittest.main()
