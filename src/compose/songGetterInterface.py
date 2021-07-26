#
# File containing code for song getter interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getSongsWithLyrics function
# getSongsWithLyrics function should return a list of objects
# Each object in the list should consist of the following attributes
# "title", "artist", "info" and "lyrics"
# In case of any errors/failures, an empty list should be returned

# Initialise class
class SongGetterInterface(ABC):

    @abstractmethod
    def getSongsWithLyrics(self):
        pass
