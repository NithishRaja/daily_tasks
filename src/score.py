#
# File containing logic to get score
#
#

# Dependencies
import requests, json
from datetime import datetime, timedelta
import dateutil.parser

# Initialise base URL
baseURL = "http://data.nba.net/10s"
# Initialise URL to get other links
URLIndex = "/prod/v2/today.json"

# Function to get links
def getLinks():
    # Send request to get all links
    res = requests.get(baseURL+URLIndex)
    # Parse response into JSON object
    links = json.loads(res.text)
    # Return links
    return links

# Function to get date
def getDate():
    # Call function to get links
    links = getLinks()
    # Return date
    return links["links"]["currentDate"]

# Function to extract game data
def extractGameData(links, scoreboard):
    # Initialise variable to hold data
    data = {}

    # Add data to object
    data["currentDate"] = links["links"]["currentDate"]
    data["standingsURL"] = "https://www.nba.com/standings"
    data["games"] = []
    data["cache"] = True

    # Iterate over games
    for game in scoreboard["games"]:
        # Check if game is over
        if not game["statusNum"] > 2:
            data["cache"] = False
        # Initialise title
        title = ""
        subtitle = ""
        # Check if game is a playoff game
        if "playoffs" in game.keys():
            title = game["playoffs"]["confName"]+" ROUND "+game["playoffs"]["roundNum"]
            subtitle = game["playoffs"]["seriesSummaryText"]
        else:
            title = game["hTeam"]["triCode"]+" vs "+game["vTeam"]["triCode"]
            subtitle = "series record: "+str(game["hTeam"]["seriesWin"])+"-"+str(game["hTeam"]["seriesLoss"])

        # Generate home team score array
        hTeamScore = []
        for score in game["hTeam"]["linescore"]:
            hTeamScore.append(score["score"])
        # Append final score
        hTeamScore.append(game["hTeam"]["score"])
        # Generate visiting team score array
        vTeamScore = []
        for score in game["vTeam"]["linescore"]:
            vTeamScore.append(score["score"])
        # Append final score
        vTeamScore.append(game["vTeam"]["score"])

        # Set clock based on status of game
        if game["statusNum"] == 1:
            # Calculate hours to game start
            startTime = dateutil.parser.isoparse(game["startTimeUTC"]).replace(tzinfo=None)
            currentTime = datetime.now()
            # Set clock based on time to start
            if startTime - currentTime < timedelta(seconds=3600):
                diff = startTime.minute - currentTime.minute
                clock = "Starts in "+str( diff if diff > 0 else (60+diff) )+" mins"
            else:
                diff = startTime.hour - currentTime.hour
                clock = "Starts in "+str( diff if diff > 0 else (24+diff) )+" hrs"
        elif game["statusNum"] == 2:
            clock = game["clock"]
        else:
            clock = "FINAL"

        # Append game data to array
        data["games"].append({
            "gameId": game["gameId"],
            "boxscoreURL": "https://global.nba.com/boxscore/#!/"+str(game["gameId"]),
            "title": title,
            "subtitle": subtitle,
            "clock": clock,
            "hTeam": {
                "id": game["hTeam"]["teamId"],
                "triCode": game["hTeam"]["triCode"],
                "score": hTeamScore
            },
            "vTeam": {
                "id": game["vTeam"]["teamId"],
                "triCode": game["vTeam"]["triCode"],
                "score": vTeamScore
            }
        })

    # Return data
    return data

# Function to get NBA scores
def getScore():
    # Iterate till success
    while(True):
        try:
            # Call function to get links
            links = getLinks()

            # Get scoreboard
            scoreboardURL = links["links"]["todayScoreboard"]
            # Get current day's scoreboard
            res = requests.get(baseURL+scoreboardURL)
            # Parse response into JSON object
            scoreboard = json.loads(res.text)

            # Exit loop
            break
        except:
            print("Failed to get score. Trying again...")

    # Call function to extract game data
    data = extractGameData(links, scoreboard);

    # Return data
    return data


# Check if module is used as script
if __name__ == "__main__":
    # Call function to get score
    score = getScore()
    # Print score details
    print(score)
