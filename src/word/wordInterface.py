#
# File containing code for abstract word class
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getWord function
# getWord function should return an object with the following fields
# "word", "wordType", "pronunciation"
# There should also be a default object with the same fields
# The default object should be returned in case of any errors/failures

# Initialise word class
class WordInterface(ABC):

    @abstractmethod
    def getWord(self):
        pass
