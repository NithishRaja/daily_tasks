#
# File to get events from calendar
#
#

# Dependencies
import sys
from ics import Calendar
from datetime import date, timedelta

# Function to get events from calendar
def getEvents(fileName, upperLimit, lowerLimit):
    # Initialise array to hold events data
    data = []

    try:
        # Open file
        file = open("./userData/"+fileName)
        # Parse calendar
        c = Calendar(file.read())
        # Close file
        file.close()
        # Convert events set into a list
        eventList = list(c.events)
        # Get today's date
        t = date.today()
        # Create timedelta for event window
        diff1 = timedelta(days=int(upperLimit))
        diff2 = timedelta(days=int(lowerLimit))
        # Iterate over events
        for event in eventList:
            # Generate event date
            d = date(year=2021, month=event.begin.month, day=event.begin.day)
            # Check if event date is within window
            if d - t < diff1 and d - t > diff2:
                data.append({
                    "name": event.name,
                    "date": str(d.day)+"/"+str(d.month)+"/"+str(d.year)
                })
    except:
        # Print error message
        print("Failed to get events.")

    return data


# Check if module is used as script
if __name__ == "__main__":
    # Call function to get events
    events = getEvents(sys.argv[1], sys.argv[2], sys.argv[3])
    # Print day
    print(events)
