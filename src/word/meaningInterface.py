#
# File containing code for abstract meaning class
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getMeaning function
# getMeaning function should accept a string as input
# It should return a list of meanings of the word passed in the string
# If the string does not contain a word or meaning doesn't exist, it should return an empty list
# In case of any errors/failures, an empty list should be returned

# Initialise meaning class
class MeaningInterface(ABC):

    @abstractmethod
    def getMeaning(self, word):
        pass
