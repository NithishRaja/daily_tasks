#
# File containing day class
#
#

# Dependencies
import sys, os
from datetime import date

sys.path.append(os.path.abspath(os.path.join("src")))

# Local Dependencies
from helpers.requestFacade import requestFacade

# Initialise class
class Day:
    # Initialise constructor
    def __init__(self):
        # Initialise baseURL
        self.baseURL = "https://www.daysoftheyear.com"
        # Initialise sender
        self.sender = requestFacade()

    # Function to get day by date
    def getDayByDate(self, day, month):
        """Function to scrape HTML for days in given date.

        Keyword Arguments:
        day -- integer
        month -- integer
        """
        # Initialise array for data
        data = []
        # Prepare URL
        URL = os.path.join(self.baseURL, "days",
                           str(date.today().year),
                           str(month).zfill(2),
                           str(day).zfill(2))
        # Call function to send request and get HTML response
        res = self.sender["HTML"](URL)
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
