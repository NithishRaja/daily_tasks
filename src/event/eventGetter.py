#
# File to get events
#
#

# Dependencies
from datetime import date
# Local Dependencies
from eventGetterInterface import EventGetterInterface
from eventInterface import EventInterface

class EventGetter(EventGetterInterface):
    def __init__(self, event: EventInterface):
        # Initialise event class
        self.eventObj = event

    # Function to get events
    def getEventList(self):
        # Get today date
        today = date.today()
        # Return list of events for today
        return self.eventObj.getEvents(today, today)
