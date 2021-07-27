#
# File containing unit tests
#
#

# Dependencies
import unittest, sys, os

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from persistInMemory import PersistInMemory

class TestPersistInMemoryMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise persist in memory object
        self.persistInMemory = PersistInMemory()
    # Test reading data success
    def test_persist_in_memory_read_data_success(self):
        # Prepare dummy data
        data = {
            "name": "glasses",
            "role": "bane of my existence"
        }
        # Store data
        self.persistInMemory.persistDataByKey("data", data)
        # Retrieve data
        res = self.persistInMemory.retrieveDataByKey("data")
        # Check response type
        self.assertIs(type(res), type(res))
        # Check attributes
        for item in data.keys():
            self.assertEqual(res[item], data[item])
    # Test reading data failure
    def test_persist_in_memory_read_data_failure(self):
        # Retrieve data
        res = self.persistInMemory.retrieveDataByKey("hohoho")
        # Check response
        self.assertEqual(res, None)
    # Tear down function
    def tearDown(self):
        del self.persistInMemory

if __name__ == "__main__":
    unittest.main()
