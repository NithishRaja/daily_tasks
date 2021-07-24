#
# File containing day class
#
#

# Dependencies
import os
from datetime import date

# Local Dependencies
from dayInterface import DayInterface

# Initialise class
class Day(DayInterface):
    # Initialise constructor
    def __init__(self, sender):
        # Initialise baseURL
        self.baseURL = "https://www.daysoftheyear.com"
        # Initialise sender
        self.sender = sender

    # Function to prepare URL
    def getURLForDate(self, day, month):
        """Generate URL for given data and return it.

        Keyword Arguments:
        day -- integer
        month -- integer
        """
        return os.path.join(self.baseURL, "days",
                           str(date.today().year),
                           str(month).zfill(2),
                           str(day).zfill(2))

    # Function to get day by date
    def getDayByDate(self, day, month):
        """Function to scrape HTML for days in given date.

        Keyword Arguments:
        day -- integer
        month -- integer
        """
        # Initialise array for data
        data = []
        # Call function to get complete URL
        URL = self.getURLForDate(day, month)
        # Call function to send request and get HTML response
        res = self.sender["HTML"](URL)
        # Check status code
        if res["status"] == 200:
            # Get list of HTML components with day info
            dayList = res["payload"].select(".section__cards")[0].select(".card__title a")
            # Extract data
            for day in dayList:
                data.append({
                    "text": day.text.replace("\xa0", " "),
                    "link": day["href"]
                })
        # Return data array
        return data
