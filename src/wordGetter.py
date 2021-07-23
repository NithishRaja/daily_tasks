#
# File containing class to get words of the day
#
#

# Dependencies
import os
# Local Dependencies
from getterInterface import GetterInterface
from word.wordComposite import WordComposite

class WordGetter(GetterInterface):
    # Define constructor
    def __init__(self):
        # Initialise object
        self.wordObj = WordComposite()

    def getData(self):
        """Get word from word obj and return the response."""
        return self.wordObj.getWord()
