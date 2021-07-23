#
# File containing word composite class
#
#

# Dependencies

# Local Dependencies
from wordInterface import WordInterface
from meaningInterface import MeaningInterface

# Initialise class
class WordComposite(WordInterface):
    # Initialise constructor
    def __init__(self, meaning: MeaningInterface):
        # Initialise word array
        self.wordObjList = []
        # Initialise meaning object
        self.meaningObj = meaning

    # Function to add word to list
    def addWord(self, word: WordInterface):
        """Append word object to list.

        Keyword Arguments:
        word -- object from class implementing WordInterface
        """
        # Append object to list
        self.wordObjList.append(word)

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
