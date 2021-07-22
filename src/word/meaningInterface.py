#
# File containing code for abstract meaning class
#
#

# Dependencies
from abc import ABC, abstractmethod

# Initialise meaning class
class MeaningInterface(ABC):

    @abstractmethod
    def getMeaning(self, word):
        pass
