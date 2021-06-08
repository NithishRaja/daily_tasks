#
# File containing logic to get score
#
#

# Dependencies
import requests, json

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

# Function to get NBA scores
def getScore():
    # Call function to get links
    links = getLinks()

    # Initialise variable to hold data
    data = {}

    # Get scoreboard
    scoreboardURL = links["links"]["todayScoreboard"]
    # Get current day's scoreboard
    res = requests.get(baseURL+scoreboardURL)
    # Parse response into JSON object
    scoreboard = json.loads(res.text)

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

        # Append game data to array
        data["games"].append({
            "gameId": game["gameId"],
            "boxscoreURL": "https://global.nba.com/boxscore/#!/"+str(game["gameId"]),
            "title": title,
            "subtitle": subtitle,
            "clock": game["clock"] if len(game["clock"]) > 0 else "--:--",
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

# Check if module is used as script
if __name__ == "__main__":
    # Call function to get score
    score = getScore()
    # Print score details
    print(score)
