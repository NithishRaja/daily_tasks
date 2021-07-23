#
# File containing code for abstract lyric class
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getLyric function
# getLyric function takes title and artist as input (both strings)
# getLyric function should return a list of list
# The list should consist of sections of the song lyric
# The internal list should consist of individual lines in a section
# In case of errors/failures, return an empty list

# Initialise lyric class
class LyricInterface(ABC):

    @abstractmethod
    def getLyric(self, title, artist):
        pass
