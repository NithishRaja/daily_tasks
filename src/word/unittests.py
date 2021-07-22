#
# File containing unit tests
#
#

# Dependencies
import unittest
# Local Dependencies
from dictionary import Dictionary
from merriam import Merriam
from meaning import Meaning
from wordComposite import WordComposite

class TestDictionaryMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise word object
        self.dictionaryObj = Dictionary()
    # Check output of dictionary class for normal request
    def test_dictionary_getWord_normal_response(self):
        # Initialise attribute list
        attributeList = ["word", "wordType", "pronunciation"]
        # Call function to get word
        word = self.dictionaryObj.getWord()
        # Check response type
        self.assertIs(type(word), type({}))
        # Check attributes in response
        for item in attributeList:
            self.assertTrue(item in word.keys())
    # Check output of dictionary class for failed request
    def test_dictionary_getWord_failed_response(self):
        # Initialise default word
        defaultWord = {
            "word": "altruism",
            "wordType": "noun",
            "pronunciation": "al-troo-iz-uhm"
        }
        # Modify URL
        self.dictionaryObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        # Call function to get word
        word = self.dictionaryObj.getWord()
        # Check response type
        self.assertIs(type(word), type({}))
        # Check attributes in response
        for item in defaultWord.keys():
            self.assertEqual(defaultWord[item], word[item])
    def tearDown(self):
        del self.dictionaryObj

class TestMerriamMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise word object
        self.merriamObj = Merriam()
    # Check output of merriam class for normal request
    def test_merriam_getWord_normal_response(self):
        # Initialise attribute list
        attributeList = ["word", "wordType", "pronunciation"]
        # Call function to get word
        word = self.merriamObj.getWord()
        # Check response type
        self.assertIs(type(word), type({}))
        # Check attributes in response
        for item in attributeList:
            self.assertTrue(item in word.keys())
    # Check output of merriam class for failed request
    def test_merriam_getWord_failed_response(self):
        # Initialise default word
        defaultWord = {
            "word": "whilom",
            "wordType": "adverb",
            "pronunciation": "whi-lom"
        }
        # Modify baseURL
        self.merriamObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        # Call function to get word
        word = self.merriamObj.getWord()
        # Check response type
        self.assertIs(type(word), type({}))
        # Check attributes in response
        for item in defaultWord.keys():
            self.assertEqual(defaultWord[item], word[item])
    def tearDown(self):
        del self.merriamObj

class TestMeaningMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise meaning object
        self.meaningObj = Meaning()
    def test_getMeaning_for_normal_response(self):
        # Initialise array of meanings
        meanings = [': to destroy to the ground : demolish', ': to scrape, cut, or shave off', ': erase']
        # Call function to get meanings
        data = self.meaningObj.getMeaning("raze")
        # Check number of entries in data returned
        self.assertEqual(len(data), 3)
        # Check data
        for item in data:
            self.assertTrue(item in meanings)
    # Check output of getMeaning for bad request
    def test_getMeaning_for_bad_response(self):
        # Call function to get meanings
        data = self.meaningObj.getMeaning("hoping this is not a word")
        self.assertEqual(len(data), 0)
    # Check output of getMeaning for failed request
    def test_getMeaning_for_no_response(self):
        # Modify baseURL
        self.meaningObj.baseURL = "https://the-internet.herokuapp.com/status_codes/404"
        # Call function to get meanings
        data = self.meaningObj.getMeaning("does not matter")
        self.assertEqual(len(data), 0)
    # Tear down function
    def tearDown(self):
        del self.meaningObj

class TestWordCompositeMethods(unittest.TestCase):
    # Set up function
    def setUp(self):
        # Initialise object
        self.wordCompositeObj = WordComposite()
    def test_word_composite_getWord(self):
        # Initialise attribute list
        attributeList = ["word", "wordType", "pronunciation", "meaning"]
        # Call function to get words
        res = self.wordCompositeObj.getWord()
        # Check type of response
        self.assertIs(type(res), type([]))
        # Check attributes of object in list
        for item in attributeList:
            self.assertTrue(item in res[0].keys())
    # Tear down function
    def tearDown(self):
        del self.wordCompositeObj


if __name__ == '__main__':
    unittest.main()
