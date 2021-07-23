#
# File containing song class
#
#

# Dependencies

# Local Dependencies
from songInterface import SongInterface

# Initialise class
class Song(SongInterface):
    # Initialise constructor
    def __init__(self, sender):
        # Initialise base URL
        self.baseURL = "https://www.billboard.com/charts/hot-100"
        # Initialise sender
        self.sender = sender

    # Function to split array of strings based on separator
    def splitString(self, stringArr, separator):
        """Iterate over each string in array and call split function on it.

        Keyword Arguments:
        stringArr -- array
        separator -- string
        """
        # Initialise array to hold results
        result = []
        # Iterate over array
        for item in stringArr:
            # Split string
            temp = item.split(separator)
            # Iterate over separated strings and add them to result
            for tempItem in temp:
                result.append(tempItem)
        # Return result
        return result

    # Function to extract data from artist string
    def parseArtistString(self, artistStr):
        """Extract artist names separated by x, &, + and 'featured'

        Keyword Arguments:
        artistStr -- string
        """
        # Initialise object to return
        result = {}
        # Split array by 'featuring'
        temp = self.splitString([artistStr], " featuring ")
        # Store artists and featured artists separately
        result["artist"] = [temp[0]]
        # Check if featured artists exists
        if len(temp) == 2:
            result["featured"] = [temp[1]]
        else:
            result["featured"] = []
        # Split strings by 'x', '&' and '+'
        for item in ["artist", "featured"]:
            # Split array by '+'
            result[item] = self.splitString(result[item], " + ")
            # Split array by 'x'
            result[item] = self.splitString(result[item], " x ")
            # Split array by '&'
            result[item] = self.splitString(result[item], " & ")
        # Return result object
        return result


    # Function to get songs
    def getSongList(self):
        """Scrape base URL for songs and extract song data."""
        # Initialise array to hold songs
        songList = []
        # Send request
        res = self.sender["HTML"](self.baseURL)
        # Check response status
        if res["status"] == 200:
            # Extract list of HTML elements with song details
            temp = res["payload"].select(".chart-element__information")
            # Iterate over each song
            for item in temp:
                songList.append({
                    "title": item.select(".chart-element__information__song")[0].text,
                    "artist": self.parseArtistString( item.select(".chart-element__information__artist")[0].text ),
                    "info": [
                        item.select(".text--last")[0].text,
                        item.select(".text--peak")[0].text,
                        item.select(".text--week")[0].text
                    ]
                })
        # Return song list
        return songList
