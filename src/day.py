#
# File to get international day
#
#

# Dependencies
import os
from datetime import date
import sys
# local Dependencies
from helpers.requestFactory import requestFactory

# Function to get current date's international day
def getDay(day, month):
    # Initialise array for data
    data = []
    # Initialise base URL
    baseURL = "https://www.daysoftheyear.com"
    # Prepare URL
    URL = os.path.join(baseURL, "days",
                       str(date.today().year),
                       str(month).zfill(2),
                       str(day).zfill(2)
                      )
    # Initialise sender
    sender = requestFactory()

    # Call function to send request and get HTML response
    res = sender["HTML"](URL)
    # Check status code
    if res["status"] == 200:
        # Get list of HTML components with day info
        dayList = res["payload"].select(".section__cards")[0].select(".card__title a")
        # Extract data
        for day in dayList:
            data.append({
                "text": day.text,
                "link": day["href"]
            })
    # Return data array
    return data

# Check if module is used as script
if __name__ == "__main__":
    # Call function to get day list
    data = getDay(day=sys.argv[1], month=sys.argv[2])
    # Print list
    print(data)
