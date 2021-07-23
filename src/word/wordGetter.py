#
# File containing class to get words of the day
#
#

# Dependencies
import os
# Local Dependencies
from getterInterface import GetterInterface
from wordInterface import WordInterface
from meaningInterface import MeaningInterface

# Initialise class
class WordGetter(GetterInterface):
    # Define constructor
    def __init__(self, word: WordInterface, meaning: MeaningInterface):
        # Initialise word object
        self.wordObj = word
        # Initialise meaning object
        self.meaningObj = meaning

    def getData(self):
        """Get word from word obj and find it's meaning.
        Return the response with meaning of each word appended to it.
        """
        # Call function to get words
        res = self.wordObj.getWord()
        # Iterate over each word
        for item in res:
            # Get meaning of word
            item["meaning"] = self.meaningObj.getMeaning(item["word"])
        # Return words
        return res
