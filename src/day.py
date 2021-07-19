#
# File to get international day
#
#

# Dependencies
import os
from datetime import date
# local Dependencies
from helpers.requestFacade import requestFacade
from getter import Getter

class Day(Getter):
    # Define constructor
    def __init__(self):
        # Initialise URL
        self.baseURL = "https://www.daysoftheyear.com"
        # Initialise date
        self.date = {
            "day": date.today().day,
            "month": date.today().month,
            "year": date.today().year
        }
        # Initialise sender
        self.sender = requestFacade()

    # Function to set the date
    def setDate(self, day, month):
        """Function to set the day and month of date variable.

        Keyword Arguments:
        day -- integer
        month -- integer
        """
        # Update date with new values
        self.date["day"] = day
        self.date["month"] = month

    def getData(self):
        """Function to scrape HTML for 'day of the year' data and return it"""
        # Initialise array for data
        data = []
        # Prepare URL
        URL = os.path.join(self.baseURL, "days",
                           str(self.date["year"]),
                           str(self.date["month"]).zfill(2),
                           str(self.date["day"]).zfill(2))
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
