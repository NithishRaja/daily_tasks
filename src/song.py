#
# File to get a song at random
#
#

# Dependencies
import requests, bs4
import random, urllib

# Function to check if string is empty or has escape characters
def checkString(s):
    if len(s) == 0 or "\r" in s:
        return False
    else:
        return True

# Function to get URL for song lyrics
def getLyricURL(title, artist):
    # Initialise baseURL
    baseURL = "https://search.azlyrics.com/search.php?q="
    # Generate URL
    listURL = baseURL+urllib.parse.quote(title+" "+artist)
    # Send request to get index
    res = requests.get(listURL)
    # Parse HTML
    resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
    # Return URL for lyrics
    return resHTML.select("td a")[0]["href"]

# Function to get song lyrics
def getLyrics(title, artist):
    # Call function to get lyricURL
    lyricURL = getLyricURL(title, artist)
    # Send request to get lyrics
    res = requests.get(lyricURL)
    # Parse HTML
    resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
    # Extract lyrics
    lyricsRaw = resHTML.find_all("div", {"class": "", "id": ""})[0].text
    # Split lyrics into lines
    lyricPara = lyricsRaw.split("\n\n")
    # Initialise array for lyrics
    lyrics = []
    # Iterate over segments in lyrics
    for lyric in lyricPara:
        # Filter empty lines and escape characters
        temp = list(filter(checkString, lyric.split("\n")))
        # Append lines
        lyrics.append( temp )
    # Return lyrics
    return lyrics

def getSong():
    # Send request to get song list
    res = requests.get("https://www.billboard.com/charts/hot-100")
    # Parse HTML
    resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
    # Get song list
    songList = resHTML.select(".chart-element__information")
    # Select a song at random
    song = songList[ random.randint(0, len(songList)-1) ]
    # Extract song title
    title = song.select(".chart-element__information__song")[0].text
    # Extract song artist
    artist = song.select(".chart-element__information__artist")[0].text
    # Call function to get song lyrics
    lyrics = getLyrics(title, artist)
    # Return song details
    return {
        "title": title,
        "artist": artist,
        "info": [
            song.select(".text--last")[0].text,
            song.select(".text--peak")[0].text,
            song.select(".text--week")[0].text
        ],
        "lyrics": lyrics
    }

# Check if module is used as script
if __name__ == "__main__":
    # Call function to get song
    song = getSong()
    # Print song details
    print(song["title"])
    print(song["artist"])
    for item in song["info"]:
        print(item)
    print(song["lyrics"])
