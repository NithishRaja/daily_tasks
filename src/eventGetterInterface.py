#
# File containing code for event getter interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getEvents function
# getEvents function takes lowerLimit and upperLimit as input (both datetime.date objects)
# getEvents function should return a list of objects
# Objects in the returned list should consist of the following fields
# "name" and "date"
# "date" should be an object itself with the fields "day", "month", "year"
# In case of errors/failures, return an empty list

# Initialise class
class EventGetterInterface(ABC):

    @abstractmethod
    def getEvents(self, lowerLimit, upperLimit):
        pass
