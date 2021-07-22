#
# File containing word composite class
#
#

# Dependencies
import sys, os

sys.path.append(os.path.abspath(os.path.join("src")))
sys.path.append(os.path.abspath(os.path.join("src", "word")))

# Local Dependencies
from meaning import Meaning
from merriam import Merriam
from dictionary import Dictionary
from wordInterface import WordInterface

# Initialise class
class WordComposite(WordInterface):
    # Initialise constructor
    def __init__(self):
        # Initialise word array
        self.wordObjList = [Dictionary(), Merriam()]
        # Initialise meaning object
        self.meaningObj = Meaning()

    # Initialise function to get words
    def getWord(self):
        """Call getWord on all objects and return them as an array."""
        # Initialise array to hold words
        wordList = []
        # Iterate over wordObjList
        for item in self.wordObjList:
            # Call function to get word
            res = item.getWord()
            # Call function to get meaning
            res["meaning"] = self.meaningObj.getMeaning(res["word"])
            # Append word to array
            wordList.append(res)
        # Return word list
        return wordList
