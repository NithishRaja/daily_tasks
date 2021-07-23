#
# File to get score
#
#

# Dependencies
from datetime import date
# Local Dependencies
from getterInterface import GetterInterface
from score.score import Score

class ScoreGetter(GetterInterface):
    def __init__(self):
        # Initialise score class
        self.scoreObj = Score()

    # Function to get events
    def getData(self):
        """Returns object with all required fields."""
        return {
            "currentDate": self.scoreObj.getCurrentDate(),
            "standingsURL": self.scoreObj.getStandingsURL(),
            "games": self.scoreObj.getScoreToday()
        }
