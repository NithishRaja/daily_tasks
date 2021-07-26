#
# File containing video class
#
#

# Dependencies

# Local Dependencies
from compose.videoGetterInterface import VideoGetterInterface

# Initialise class
class VideoGetter(VideoGetterInterface):
    # Initialise constructor
    def __init__(self, sender):
        # Initialise base URL
        self.baseURL = "https://www.googleapis.com/youtube/v3/search?"
        # Initialise sender
        self.sender = sender
        # Initialise key
        self.key = ""

    # Function to add API key
    def addKey(self, key):
        """Store the key parameter in a variable.

        Keyword Arguments:
        key -- string
        """
        self.key = key

    # Function to get video URL
    def getVideoURL(self, searchString):
        """Return URL of a video corresponding to given searchString.

        Keyword Arguments:
        searchString -- string
        """
        # Initialise variable to hold result
        result = None
        # Send request
        res = self.sender["JSON"](self.baseURL+"q="+searchString+"&maxResults=1&key="+self.key)
        # Check response status
        if res["status"] == 200:
            # Check number of results
            if not res["payload"]["pageInfo"]["totalResults"] == 0:
                result = "https://www.youtube.com/watch?v="+res["payload"]["items"][0]["id"]["videoId"]
        # Return result
        return result
