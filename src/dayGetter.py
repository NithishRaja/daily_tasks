#
# File to get international day
#
#

# Dependencies
from datetime import date

# local Dependencies
from getter import Getter
from day.day import Day

class DayGetter(Getter):
    # Define constructor
    def __init__(self):
        # Initialise day object
        self.dayObj = Day()

    # Get data function
    def getData(self):
        """Returns data from day object."""
        return self.dayObj.getDayByDate(day=date.today().day, month=date.today().month)