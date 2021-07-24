#
# File containing code for event getter interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getEventList function
# getEventList function should return a list
# In case of any errors/failures, an empty list should be returned

# Initialise class
class EventGetterInterface(ABC):

    @abstractmethod
    def getEventList(self):
        pass
