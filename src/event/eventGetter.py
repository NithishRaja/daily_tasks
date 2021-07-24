#
# File to get events
#
#

# Dependencies
import random, sys
from datetime import date
# Local Dependencies
from getterInterface import GetterInterface
from event import Event

class EventGetter(GetterInterface):
    def __init__(self):
        # Initialise event class
        self.eventObj = Event("/home/python/userData/file.ics")

    # Function to get events
    def getData(self):
        # Get today date
        today = date.today()
        # Return list of events for today
        return self.eventObj.getEvents(today, today)
