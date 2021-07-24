#
# File containing code for day getter interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getDayList function
# getDayList function should return a list of strings
# In case of any errors/failures, an empty list should be returned

# Initialise class
class DayGetterInterface(ABC):

    @abstractmethod
    def getDayList(self):
        pass
