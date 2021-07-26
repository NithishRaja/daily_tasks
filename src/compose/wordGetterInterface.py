#
# File containing code for word getter interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getWordWithMeaning function
# getWordWithMeaning function should return a list of objects
# Each object in the list should consist of the following attributes
# "word", "wordType", "pronunciation" and "meaning"
# In case of any errors/failures, an empty list should be returned

# Initialise class
class WordGetterInterface(ABC):

    @abstractmethod
    def getWordWithMeaning(self):
        pass
