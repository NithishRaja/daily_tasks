#
# File containing code for abstract word class
#
#

# Dependencies
from abc import ABC, abstractmethod

# Initialise word class
class WordInterface(ABC):

    @abstractmethod
    def getWord(self):
        pass
