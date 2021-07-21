#
# File containing unit tests for event class
#
#

# Dependencies
import unittest, sys, os
from datetime import date
# Local Dependencies
from event import Event

class TestEventMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise base path
        self.basePath = os.path.join(sys.path[0], "testICS")
        # Initialise quote object
        self.eventObj = Event(os.path.join(self.basePath, "default.ics"))
    # Functions to test get events for normal response
    def test_get_events_normal_response_single_day(self):
        # Initialise startDate and endDate
        startDate = date(year=date.today().year, month=10, day=10)
        endDate = date(year=date.today().year, month=10, day=10)
        # Get response
        res = self.eventObj.getEvents(startDate, endDate)
        # Check type of response
        self.assertEqual(type(res), type([]))
        # Check length of array
        self.assertEqual(len(res), 2)
    def test_get_events_normal_response_range(self):
        # Initialise attribute array
        attributeList = ["name", "date"]
        # Initialise startDate and endDate
        startDate = date(year=date.today().year, month=10, day=10)
        endDate = date(year=date.today().year, month=10, day=20)
        # Get response
        res = self.eventObj.getEvents(startDate, endDate)
        # Check type of response
        self.assertEqual(type(res), type([]))
        # Check length of array
        self.assertEqual(len(res), 3)
        # Iterate over arrtibutes
        for item in res[0].keys():
            self.assertTrue(item in attributeList)
    # Function to test get events for empty response
    def test_get_events_empty_response(self):
        # Initialise startDate and endDate
        startDate = date(year=date.today().year, month=1, day=10)
        endDate = date(year=date.today().year, month=1, day=20)
        # Get response
        res = self.eventObj.getEvents(startDate, endDate)
        # Check type of response
        self.assertEqual(type(res), type([]))
        # Check length of array
        self.assertEqual(len(res), 0)
    # Function to test get events for empty file
    def test_get_events_empty_file(self):
        # Initialise startDate and endDate
        startDate = date(year=date.today().year, month=10, day=10)
        endDate = date(year=date.today().year, month=10, day=20)
        # Initialise object
        eventObj = Event(os.path.join(self.basePath, "empty.ics"))
        # Get response
        res = eventObj.getEvents(startDate, endDate)
        # Check type of response
        self.assertEqual(type(res), type([]))
        # Check length of array
        self.assertEqual(len(res), 0)
    # Function to test for file not exists
    def test_get_events_empty_file(self):
        # Initialise startDate and endDate
        startDate = date(year=date.today().year, month=10, day=10)
        endDate = date(year=date.today().year, month=10, day=20)
        # Initialise object
        eventObj = Event(os.path.join(self.basePath, "doesNotExist.ics"))
        # Get response
        res = eventObj.getEvents(startDate, endDate)
        # Check type of response
        self.assertEqual(type(res), type([]))
        # Check length of array
        self.assertEqual(len(res), 0)
    # Tear down function
    def tearDown(self):
        del self.eventObj

if __name__ == "__main__":
    unittest.main()
