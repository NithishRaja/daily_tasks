#
# File containing abstract class for tweet getter interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getTweetList function
# getTweetList function takes searchString as input
# getTweetList function should return a list of objects with the following fields
# "id", "text", "name", "username" and "profile_image_url"
# In case of errors/failures, return an empty list

# Initialise class
class TweetGetterInterface(ABC):

    @abstractmethod
    def getTweetList(self, searchString):
        pass
