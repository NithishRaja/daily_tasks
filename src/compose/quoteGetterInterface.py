#
# File containing code for quote getter interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getQuoteList function
# getQuoteList function should return an object with the following fields
# "topic" and "quotes"
# Quotes should be a list of objects and those qbjects should have the following fields
# "text" and "author"
# In case of errors/failures, a default quote should be returned with the same fields

# Initialise class
class QuoteGetterInterface(ABC):

    @abstractmethod
    def getQuoteList(self):
        pass
