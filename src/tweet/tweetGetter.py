#
# File containing tweet getter class
#
#

# Dependencies

# Local Dependencies
from compose.tweetGetterInterface import TweetGetterInterface

# Initialise class
class TweetGetter(TweetGetterInterface):
    # Initialise constructor
    def __init__(self, sender):
        # Initialise base URL
        self.baseURL = "https://api.twitter.com/2"
        # Initialise tweet count
        self.tweetCount = 3
        # Initialise variable for token
        self.APIToken = ""
        # Initialise sender
        self.sender = sender

    # Function to store API token
    def addToken(self, token):
        """Store the API token passed as parameter.

        Keyword Arguments:
        token -- string
        """
        self.APIToken = token

    # Function to replace shortened urls in text
    def replaceURL(self, text, urls):
        """Replace list of shortened URL with their original ones in text.

        Keyword Arguments:
        text -- string
        urls -- array
        """
        # Switch to original URLs
        for url in urls:
            text = text.replace(url["url"], url["expanded_url"])
        # Check if tweet has any URLs
        if len(urls) > 0:
            # Remove trailing tweet url
            text = text.split(" ")
            text.pop()
            text = " ".join(text)
        return text

    # Function to annotate text based on special characters.
    def annotateText(self, text):
        """Mark words beginning with '#' or '@'.

        Keyword Arguments:
        text -- string
        """
        # Initialise variable for annotated text
        annotatedText = []
        # Initialise temp variable to hold string
        previous = ""
        # Initialise flag
        flag = True
        # Iterate over text
        for j in range(len(text)):
            # Check if previous string is text
            if flag:
                # Check if current character is hashtag
                if text[j] == "#" or text[j] == "@":
                    if len(previous) > 0:
                        # Push previous into array
                        annotatedText.append({"text": previous, "type": "text"})
                    # Reset previous
                    previous = ""
                    # Update flag
                    flag = False
            else:
                # Check if current character is space
                if text[j] == " ":
                    if len(previous) > 0:
                        # Push previous into array
                        annotatedText.append({"text": previous, "type": "special"})
                    # Reset previous
                    previous = ""
                    # Update flag
                    flag = True
            # Add current character to previous
            previous = previous + text[j]

        if len(previous) > 0:
            # Push previous into array
            annotatedText.append({"text": previous, "type": "text" if flag else "hashtag"})
        # Return annotated text
        return annotatedText

    # Function to generate tweet URL
    def generateTweetURL(self, searchString):
        """Generates and returns URL to get tweets matching search string.

        Keyword Arguments:
        searchString -- string
        """
        # Generate URL
        url = self.baseURL+"/tweets/search/recent?query="
        url = url+searchString
        url = url+" lang:en -is:reply -is:retweet"
        url = url+"&max_results=10"
        url = url+"&tweet.fields=attachments,author_id,context_annotations,created_at,entities,id,text"
        # Return url
        return url

    # Function to generate user URL
    def generateUserURL(self, userID):
        """Generates and returns URL to get user matching userID.

        Keyword Arguments:
        userID -- string
        """
        # Generate URL
        url = self.baseURL+"/users/"+userID+"?"
        url = url+"&user.fields=id,name,profile_image_url,username,verified"
        # Return url
        return url

    # Function to extract data from tweet and user
    def extractData(self, tweetObj, userObj):
        """Extract and return relevant information from user and tweet.

        Keyword Arguments:
        tweetObj -- dictionary
        userObj -- dictionary
        """
        return {
            "name": userObj["data"]["name"],
            "username": userObj["data"]["username"],
            "profile_image_url": userObj["data"]["profile_image_url"]
        }

    # Function to get tweets
    def getTweetList(self, searchString):
        """Connect with twitter api and get tweets matching searchString.

        Keyword Arguments:
        searchString -- string
        """
        # Initialise variable to hold tweets
        tweetList = []

        # Send request to get tweets
        res = self.sender["JSON"](self.generateTweetURL(searchString), headers={"Authorization": "Bearer "+self.APIToken})
        # Check status
        if res["status"] == 200:
            # Parse json
            tweetObj = res["payload"]
            # Check no of tweets returned
            if not tweetObj["meta"]["result_count"] == 0:
                # Iterate over results
                for i in range(self.tweetCount):
                    # Send request to get user info
                    userRes = self.sender["JSON"](self.generateUserURL(tweetObj["data"][i]["author_id"]), headers={"Authorization": "Bearer "+self.APIToken})
                    # Parse json
                    userObj = userRes["payload"]

                    # Call function to extract data from tweet and user
                    data = self.extractData(tweetObj, userObj)
                    # Add tweet id to data
                    data["id"] = tweetObj["data"][i]["id"]
                    # Check if tweet has URLs
                    if "entities" in tweetObj["data"][i].keys():
                        if "urls" in tweetObj["data"][i]["entities"].keys():
                            # Replace URLs
                            tweetObj["data"][i]["text"] = self.replaceURL(tweetObj["data"][i]["text"], tweetObj["data"][i]["entities"]["urls"])
                    # Call function to annotate text
                    data["text"] = self.annotateText(tweetObj["data"][i]["text"])

                    # Add data to array
                    tweetList.append(data)
        # Return tweet list
        return tweetList
