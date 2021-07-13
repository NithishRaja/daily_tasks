#
# File to get international day
#
#

# Dependencies
import requests, bs4, os
from datetime import date
import sys

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
    # Iterate till success
    while(True):
        try:
            # Send request to get international day
            res = requests.get(URL)
            # Parse HTML
            resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
            # Get text
            dayList = resHTML.select(".section__cards")[0].select(".card__title a")
            # Iterate over list
            for day in dayList:
                data.append({
                    "text": day.text,
                    "link": day["href"]
                })
            # Exit loop
            break
        except:
            # Print error message
            print("Failed to get day. Trying again...")
            # Reset data array
            data = []
    # Return data array
    return data

# Check if module is used as script
if __name__ == "__main__":
    # Call function to get day list
    data = getDay(day=sys.argv[1], month=sys.argv[2])
    # Print list
    print(data)
