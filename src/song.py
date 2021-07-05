#
# File to get a song at random
#
#

# Dependencies
import requests, bs4, json
import random, urllib
import sys

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
    # Initialise array for lyric paragraph
    lyricPara = []
    # Check for errors
    try:
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
    except:
        # Print error message
        print("Failed to get lyrics.")
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

def getVideo(title, artist, key):
    # Initialise object to hold video URLs
    obj = {}
    # Iterate till success
    while(True):
        try:
            # Send request to get song video URL
            res = requests.get("https://www.googleapis.com/youtube/v3/search?q="+title+" "+artist+"&maxResults=1&key="+key)
            # Parse JSON
            info = json.loads(res.text)
            # Update object with video URL
            obj["watch"] = "https://www.youtube.com/watch?v="+info["items"][0]["id"]["videoId"]
            # Send request to get song lyric video URL
            res = requests.get("https://www.googleapis.com/youtube/v3/search?q="+title+" "+artist+" lyrics"+"&maxResults=1&key="+key)
            # Parse JSON
            info = json.loads(res.text)
            # Update object with video URL
            obj["lyrics"] = "https://www.youtube.com/watch?v="+info["items"][0]["id"]["videoId"]
            # Exit loop
            break
        except:
            # Print error message
            print("Failed to get song video links. Trying again...")
    # Return object
    return obj

def getSong(key):
    # Iterate till success
    while(True):
        try:
            # Send request to get song list
            res = requests.get("https://www.billboard.com/charts/hot-100")
            # Parse HTML
            resHTML = bs4.BeautifulSoup(res.text, features="html.parser")
            # Get song list
            songList = resHTML.select(".chart-element__information")
            # Select a song at random
            song = songList[ random.randint(0, len(songList)-1) ]
            # Exit loop
            break
        except:
            # Print error message
            print("Failed to get song. Trying again...")
    # Extract song title
    title = song.select(".chart-element__information__song")[0].text
    # Extract song artist
    artist = song.select(".chart-element__information__artist")[0].text
    # Call function to get video URL
    video = getVideo(title, artist, key)
    # Process artist string
    artistStr = artist.lower()
    # Remove featured artists
    artistStr = artistStr.split(" featuring ")[0]
    # Remove 'x' when multiple artists are involved
    artistStr = artistStr.replace(" x ", " ")
    # Call function to get song lyrics
    lyrics = getLyrics(title, artistStr)
    # Return song details
    return {
        "title": title,
        "artist": artist,
        "info": [
            song.select(".text--last")[0].text,
            song.select(".text--peak")[0].text,
            song.select(".text--week")[0].text
        ],
        "lyrics": lyrics,
        "video": video
    }

# Check if module is used as script
if __name__ == "__main__":
    # Call function to get song
    song = getSong(sys.argv[1])
    # Print song details
    print(song["title"])
    print(song["artist"])
    for item in song["info"]:
        print(item)
    print(song["lyrics"])
