#
# File containing unit tests
#
#

# Dependencies
import unittest, requests, sys, os, json, time

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from webUI import WebUI
from persistence.persistInMemory import PersistInMemory

class TestWebUIMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise persist in memory object
        persistInMemoryObj = PersistInMemory()
        # Prepare data
        self.dataDict = {
            "song": {
                "title": "t",
                "info": ["1", "2", "3"],
                "artist": {"artist": ["1", "2"], "featured": ["3", "4"]},
                "video": {"watch": "w", "lyric": "l"},
                "lyrics": [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
            },
            "event": [{"name":"name1", "date":"date1"}, {"name":"name2", "date":"date2"}],
            "quote": {"topic": "dummy topic", "text": "dummy text", "author": "dummy"},
            "score": "simple string",
            "day": {"text": "text", "link": "link"},
            "word": [
                {"word": "w1", "pronunciation": "p1", "wordType": "t1", "meaning": "m1"},
                {"word": "w2", "pronunciation": "p2", "wordType": "t2", "meaning": "m2"}
            ]
        }
        # Add data to persistence object
        for item in self.dataDict.keys():
            persistInMemoryObj.persistDataByKey(item, self.dataDict[item])
        # Initialise web UI object
        self.webUIObj = WebUI(persistInMemoryObj)
        # Call function to start display
        self.webUIObj.beginDisplay()
        # Wait for server to come online
        time.sleep(5)

    # Check status code for home
    def test_web_ui_home_status_code(self):
        # Send request to home page
        res = requests.get("http://localhost:8000/")
        # Check response status code
        self.assertEqual(res.status_code, 200)

    # Check data by key
    def test_wbe_ui_data_by_key_success(self):
        # Iterate over keys in dictionary
        for item in self.dataDict.keys():
            # Send request to data
            res = requests.get("http://localhost:8000/data?key="+item)
            # Check status code
            self.assertEqual(res.status_code, 200)
            # Check data
            data = json.loads(res.text)
            # Check data in response with data dict
            self.assertEqual(data, self.dataDict[item])

    # Check data by key
    def test_wbe_ui_data_by_key_bad_request(self):
        # Send request to data
        res = requests.get("http://localhost:8000/data")
        # Check status code
        self.assertEqual(res.status_code, 400)

    # Check data by key
    def test_wbe_ui_data_by_key_not_found(self):
        # Send request to data
        res = requests.get("http://localhost:8000/data?key=doesnotexist")
        # Check status code
        self.assertEqual(res.status_code, 404)

    # Tear down function
    def tearDown(self):
        # Call function to stop display
        self.webUIObj.endDisplay()
        del self.webUIObj
        del self.dataDict

if __name__ == "__main__":
    unittest.main()
