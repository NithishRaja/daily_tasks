#
# File containing logic to get tweets
#
#

# Dependencies
import requests, json, sys

# Function to parse and annotate tweet text
def parseText(text, urls):
    # Switch to original URLs
    for url in urls:
        text = text.replace(url["url"], url["expanded_url"])
    # Check if tweet has any URLs
    if len(urls) > 0:
        # Remove trailing tweet url
        text = text.split(" ")
        text.pop()
        text = " ".join(text)
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

# Function to get tweets
def getTweet(searchKey, token, count):
    # Initialise variable to hold tweets
    tweets = []
    # Check if count is within 1 to 10
    if int(count) > 10 or int(count) < 1:
        count = 3

    # Initialise base URL
    baseURL = "https://api.twitter.com/2"
    # Generate URL
    url = baseURL+"/tweets/search/recent?query="
    url = url+searchKey
    url = url+" lang:en is:verified -is:reply -is:retweet"
    url = url+"&max_results=10"
    url = url+"&tweet.fields=attachments,author_id,context_annotations,created_at,entities,id,text"

    try:
        # Send request to get tweets
        res = requests.get(url, headers={"Authorization": "Bearer "+token})
        # Parse json
        obj = json.loads(res.text)
        # Iterate over results
        for i in range(int(count)):
            # Get user id
            user = obj["data"][i]["author_id"]
            # Generate URL
            url = baseURL+"/users/"+user+"?"
            url = url+"&user.fields=id,name,profile_image_url,username,verified"
            # Send request to get user info
            res = requests.get(url, headers={"Authorization": "Bearer "+token})
            # Parse json
            userObj = json.loads(res.text)

            # Call function to parse text
            annotatedText = parseText(obj["data"][i]["text"], obj["data"][i]["entities"]["urls"])

            # Add data to array
            tweets.append({
                "text": annotatedText,
                "name": userObj["data"]["name"],
                "username": userObj["data"]["username"],
                "profile_image_url": userObj["data"]["profile_image_url"],
                "profile_url": "https://twitter.com/"+userObj["data"]["username"],
                "tweet_url": "https://twitter.com/"+userObj["data"]["username"]+"/status/"+obj["data"][i]["id"],
                "verified": userObj["data"]["verified"]
            })
    except:
        # Print error message
        print("Failed to get tweets. Trying again...")

    # Return tweets
    return tweets

# Check if module is used as script
if __name__ == "__main__":
    # Call function to get tweet
    tweet = getTweet(sys.argv[1], sys.argv[2], sys.argv[3])
    # Iterate over tweets
    for t in tweet:
        print(t)
