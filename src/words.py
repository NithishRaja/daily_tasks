#
# File to get words of the day
#
#

# Dependencies
import requests, bs4, os

# Initialise global variables
baseURL1 = "https://www.merriam-webster.com"
baseURL2 = "https://www.dictionary.com"

# Function to get meaning of word
def getMeaning(word):
    # Initialise array to hold results
    data = []
    try:
        # Send request to get meaning of word
        res = requests.get(os.path.join(baseURL1, "dictionary", word))
        # Parse HTML
        resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
        # Get text
        meaningList = resHTML.select("#dictionary-entry-1 .dtText")
        # Append meaning to array
        for item in meaningList:
            data.append(item.text)
    except:
        # Print error message
        print("Failed to get meaning of "+word)
    # Return data
    return data

# Function to get current date's international day
def getWords():
    # Initialise array to store data
    data = []

    # Prepare URL
    URL1 = os.path.join(baseURL1, "word-of-the-day")
    # Iterate till success
    while(True):
        try:
            # Send request to get word from webster
            res = requests.get(URL1)
            # Parse HTML
            resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
            # Get word
            word = resHTML.select(".word-and-pronunciation h1")[0].text
            # Get syllables and word pronunciation
            wordAttrs = resHTML.select(".word-attributes")[0]
            wordType = wordAttrs.select(".main-attr")[0].text
            pronunciation = wordAttrs.select(".word-syllables")[0].text
            # Exit loop
            break
        except:
            # Print error message
            print("Failed to get word from webster. Trying again...")

    # Append object to data
    data.append({
        "word": word,
        "pronunciation": pronunciation,
        "wordType": wordType,
        "meaning": getMeaning(word)
    })

    # Prepare URL
    URL2 = os.path.join(baseURL2, "e", "word-of-the-day")
    # Iterate till success
    while(True):
        try:
            # Send request to get word from webster
            res = requests.get(URL2)
            # Parse HTML
            resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
            # Get word
            wordBlock = resHTML.select(".otd-item-headword")[0]
            word = wordBlock.select(".otd-item-headword__word h1")[0].text
            # Get syllables and word pronunciation
            pronunciation = wordBlock.select(".otd-item-headword__pronunciation")[0].text
            pronunciation = pronunciation.replace("\n", "").replace(" ", "").replace("[", "").replace("]", "")
            wordType = wordBlock.select(".otd-item-headword__pos p")[0].text.replace("\n", "").replace(" ", "")
            # Exit loop
            break
        except:
            # Print error message
            print("Failed to get word from dictionary.com. Trying again...")

    # Append object to data
    data.append({
        "word": word,
        "pronunciation": pronunciation,
        "wordType": wordType,
        "meaning": getMeaning(word)
    })

    # Return data
    return data

# Check if module is used as script
if __name__ == "__main__":
    # Call function to get words
    words = getWords()
    # Print day
    print(words)
