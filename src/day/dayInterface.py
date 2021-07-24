#
# File containing code for abstract day class
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getDayByDate function
# getDayByDate function takes day and month as input (both integers)
# getDayByDate function should return a list of strings
# In case of errors/failures, return an empty list

# Initialise Day class
class DayInterface(ABC):

    @abstractmethod
    def getDayByDate(self, day, month):
        pass
