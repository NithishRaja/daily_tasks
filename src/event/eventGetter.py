#
# File containing class to get events
#
#

# Dependencies
import os
from ics import Calendar
from datetime import date, timedelta

# Local Dependencies
from compose.eventGetterInterface import EventGetterInterface

# Initialise class
class EventGetter(EventGetterInterface):
    # Initialise constructor
    def __init__(self, filePath):
        # Initialise file path
        self.filePath = filePath
        # Initialise array to hold events
        self.events = []

        # Call function to read events file
        self.readEvents()

    # Function to read events
    def readEvents(self):
        """Read in events from ics file if it exists."""
        # Check if file exists
        if os.path.exists(self.filePath):
            # Open file
            file = open(self.filePath)
            # Parse calendar
            calendar = Calendar(file.read())
            # Close file
            file.close()
            # Convert events set into a list
            self.events = list(calendar.events)

    # Function to get events in given range
    def getEvents(self, lowerLimit, upperLimit):
        """Iterate over all events and return events within given range.

        Keyword Arguments:
        lowerLimit -- Date
        upperLimit -- Date
        """
        # Initialise array to hold results
        results = []
        # Iterate over events
        for item in self.events:
            # Get date of current event
            d = date(year=date.today().year, month=item.begin.month, day=item.begin.day)
            # Check if current event is within limits
            if  d >= lowerLimit and d <= upperLimit:
                # Add event to results
                results.append({
                    "name": item.name,
                    "date": {
                        "day": d.day,
                        "month": d.month,
                        "year": d.year
                    }
                })
        # Return results
        return results
