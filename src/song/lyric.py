#
# File containing lyric class
#
#

# Dependencies
import urllib

# Local Dependencies

# Initialise class
class Lyric:
    # Initialise constructor
    def __init__(self, sender):
        # Initialise baseURL
        self.baseURL = "https://search.azlyrics.com"
        # Initialise sender
        self.sender = sender

    # Function to check if string is empty or has escape characters
    def checkString(self, s):
        if len(s) == 0 or "\r" in s:
            return False
        else:
            return True

    # Function to get URL to site containing lyrics based on search string
    def getLyricURL(self, searchString):
        """Scrape HTML for url to site with lyrics for given searchString.

        Keyword Arguments:
        searchString -- string
        """
        # Initialise empty string for result
        result = ""
        # Prepare URL
        URL = self.baseURL + "/search.php?q=" + urllib.parse.quote(searchString)
        # Send request
        res = self.sender["HTML"](URL)
        # Check response status
        if res["status"] == 200:
            # Get URL
            temp = res["payload"].select("td a")
            # Check if temp is empty
            if not len(temp) == 0:
                result = temp[0]["href"]
        # Return result
        return result

    # Function to get lyrics of given song
    def getLyric(self, title, artist):
        """Scrape HTML for song lyrics and parse the text.

        Keyword Arguments:
        title -- string
        artist -- string
        """
        # Initialise array to hold lyrics
        lyrics = []
        # Call function to get url
        URL = self.getLyricURL(title+" "+artist)
        # Check if URL is an empty string
        if not URL == "":
            # Send request
            res = self.sender["HTML"](URL)
            # Check response status
            if res["status"] == 200:
                temp = res["payload"].find_all("div", {"class": "", "id": ""})[0].text
                temp = temp.split("\n\n")
                for item in temp:
                    # Append lines
                    lyrics.append( list(filter(self.checkString, item.split("\n"))) )
        # Return lyrics
        return lyrics
