#
# File to get international day
#
#

# Dependencies
from datetime import date

# local Dependencies
from getterInterface import GetterInterface
from dayInterface import DayInterface

class DayGetter(GetterInterface):
    # Define constructor
    def __init__(self, day: DayInterface):
        # Initialise day object
        self.dayObj = day

    # Get data function
    def getData(self):
        """Returns data from day object."""
        return self.dayObj.getDayByDate(day=date.today().day, month=date.today().month)
