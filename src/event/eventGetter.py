#
# File to get events
#
#

# Dependencies
import random, sys
from datetime import date
# Local Dependencies
from getterInterface import GetterInterface
from eventInterface import EventInterface

class EventGetter(GetterInterface):
    def __init__(self, event: EventInterface):
        # Initialise event class
        self.eventObj = event

    # Function to get events
    def getData(self):
        # Get today date
        today = date.today()
        # Return list of events for today
        return self.eventObj.getEvents(today, today)
