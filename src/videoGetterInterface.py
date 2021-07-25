#
# File containing abstract class for video getter interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getVideoURL function
# getVideoURL function takes searchString as input
# getVideoURL function should return a URL to a video
# In case of errors/failures, return None

# Initialise class
class VideoGetterInterface(ABC):

    @abstractmethod
    def getVideoURL(self, searchString):
        pass
