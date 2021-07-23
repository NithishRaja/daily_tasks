#
# File containing code for abstract song class
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getSongList function
# getSongList function should return a list
# Each element in list should be an object with the following fields
# "title", "artist" and "info"
# An empty list should be returned in case of any errors/failures

# Initialise song class
class SongInterface(ABC):

    @abstractmethod
    def getSongList(self):
        pass
