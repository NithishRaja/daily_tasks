#
# File containing code for score getter interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a getScoreByDay and getCurrentDate functions
# getScoreByDay function takes dateString (YYYYMMDD) as input
# getScoreByDay function should return a list of objects
# Objects in the returned list should consist of the following fields
# "gameId", "boxscoreURL", "title", "subtitle", "hTeam", "vTeam" and "clock"
# "hTeam" and "vTeam" should themselves be objects with the following attributes
# "id", "triCode" and "score"
# In case of errors/failures, return an empty list

# Initialise class
class ScoreGetterInterface(ABC):

    @abstractmethod
    def getScoreByDay(self, dateString):
        pass

    @abstractmethod
    def getCurrentDate(self):
        pass
