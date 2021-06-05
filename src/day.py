#
# File to get international day
#
#

# Dependencies
import requests, bs4
import random, os
from datetime import date

# Function to get current date's international day
def getDay():
    # Initialise base URL
    baseURL = "https://www.daysoftheyear.com"
    # Prepare URL
    URL = os.path.join(baseURL, "days",
                       str(date.today().year),
                       str(date.today().month).zfill(2),
                       str(date.today().day).zfill(2)
                      )
    # Send request to get international day
    res = requests.get(URL)
    # Parse HTML
    resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
    # Get text
    dayList = resHTML.select(".section__cards")[0].select(".card__title a")
    # Select day at random
    day = dayList[ random.randint(0, len(dayList)-1) ]
    # Return day
    return {
        "text": day.text,
        "link": day["href"]
    }

# Check if module is used as script
if __name__ == "__main__":
    # Call function to get day
    day = getDay()
    # Print day
    print(day["text"])
