#
# File to get quote
#
#

# Dependencies
import requests, bs4
import random

# Initialise baseURL for quotes
quotesURL = "https://www.brainyquote.com"

# Function to get topic index
def getTopicIndex():
    # Send request to get topics index
    res = requests.get(quotesURL+"/topics")
    # Parse HTML
    resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
    # Get text
    index = resHTML.select(".bq_s .bq_fl .bqLn a")
    # Select random index
    indexURL = index[ random.randint(0, len(index)-1) ]["href"]
    # Return indexURL
    return indexURL

# Function to get specific topic
def getTopic():
    # Call function to get topic index
    indexURL = getTopicIndex()
    # Send request to get topics
    res = requests.get(quotesURL+indexURL)
    # Parse HTML
    resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
    # Get topics list
    topicList = resHTML.select(".bqLn a")
    # Select random topic
    topic = topicList[ random.randint(0, len(topicList)-1) ]
    # Return topicURL and topic
    return {
        "url": topic["href"],
        "text": topic.text
    }

# Function to get a quote at random
def getQuote():
    # Call function to get topic
    topic = getTopic()
    # Send request to get topics index
    res = requests.get(quotesURL+topic["url"])
    # Parse HTML
    resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
    # Get quote list
    quoteList = resHTML.select("#quotesList .bqQt")
    # Select random quote
    quote = quoteList[ random.randint(0, len(quoteList)-1) ]
    # Get quote text
    quoteText = quote.find("a", {"title": "view quote"}).text
    # Get quote author
    quoteAuthor = quote.find("a", {"title": "view author"}).text
    # Return topic, quote and author
    return {
        "topic": topic["text"],
        "quote": quoteText,
        "author": quoteAuthor
    }

# Check if module is used as script
if __name__ == "__main__":
    # Call function to get quote
    quote = getQuote()
    # Print quote
    print(quote["topic"])
    print(quote["quote"])
    print(quote["author"])
