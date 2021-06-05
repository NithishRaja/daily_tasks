#
# Index File
#
#

# Dependencies
import json
# Local dependencies
from src.day import getDay
from src.quote import getQuote
from src.song import getSong

try:
    # Call function to get day
    day = getDay()
    # Print day
    print(day["text"])
    # Open file
    file = open("./data/day.json", "w")
    # Write to file
    json.dump(day, file)
    # Close file
    file.close()
except:
    print("failed to get day")

try:
    # Call function to get quote
    quote = getQuote()
    # Print quote
    print(quote["topic"])
    print(quote["quote"])
    print(quote["author"])
    # Open file
    file = open("./data/quote.json", "w")
    # Write to file
    json.dump(quote, file)
    # Close file
    file.close()
except:
    print("failed to get quote")

try:
    # Call function to get song
    song = getSong()
    # Print song details
    print(song["title"])
    print(song["artist"])
    for item in song["info"]:
        print(item)
    print(song["lyrics"])
    # Open file
    file = open("./data/song.json", "w")
    # Write to file
    json.dump(song, file)
    # Close file
    file.close()
except:
    print("failed to get song")
