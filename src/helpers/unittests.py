#
# File containing code to test helper functions
#
#

# Dependencies
import unittest, bs4
# Local Dependencies
from sendRequests import send_request

# Test class
class TestHelperMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        self.sender = send_request()
    # Check send_request function for 200 status code
    def test_send_request_for_status_code_200(self):
        res = self.sender["RAW"]("https://the-internet.herokuapp.com/status_codes/200")
        self.assertEqual(res["status"], 200)
    # Check send_request function for 404 status code
    def test_send_request_for_status_code_404(self):
        res = self.sender["RAW"]("https://the-internet.herokuapp.com/status_codes/404")
        self.assertEqual(res["status"], 404)
    # Check send_request function for 500 status code
    def test_send_request_for_status_code_500(self):
        res = self.sender["RAW"]("https://the-internet.herokuapp.com/status_codes/500")
        self.assertEqual(res["status"], 500)
    # Check send_request function for JSON payload
    def test_send_request_for_JSON_payload(self):
        res = self.sender["JSON"]("http://data.nba.net/10s/prod/v2/today.json")
        self.assertEqual(type(res["payload"]), type({}))
    # Check send_request function for HTML payload
    def test_send_request_for_HTML_payload(self):
        res = self.sender["HTML"]("https://the-internet.herokuapp.com/status_codes/200")
        self.assertEqual(type(res["payload"]), type( bs4.BeautifulSoup("", features="html.parser") ))
    # Tear down function
    def tearDown(self):
        del self.sender

if __name__ == '__main__':
    unittest.main()
