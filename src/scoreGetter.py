#
# File to get score
#
#

# Dependencies
from datetime import date
# Local Dependencies
from getter import Getter
from score.score import Score

class ScoreGetter(Getter):
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
