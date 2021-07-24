#
# File containing class to get Score
#
#

# Dependencies
from datetime import datetime, timedelta
import dateutil

# Local Dependencies
from scoreGetterInterface import ScoreGetterInterface

# Initialise class
class ScoreGetter(ScoreGetterInterface):
    # Initialise constructor
    def __init__(self, sender):
        # Initialise URLs
        self.baseURL = "http://data.nba.net/10s"
        self.URLIndex = "/prod/v2/today.json"
        # Initialise object to store links
        self.links = {}
        # Initialise sender
        self.sender = sender

        # Call function to populate links
        self.getLinks()

    # Function to get all URLs
    def getLinks(self):
        """Sends a request and extract all necessary URLs from response."""
        # Send request
        res = self.sender["JSON"](self.baseURL+self.URLIndex)
        # Check response status
        if res["status"] == 200:
            # Persist URLs
            self.links = res["payload"]

    # Function to extract game scoreline
    def extractGameScoreline(self, game):
        """move scoreline of each team into array and return the arrays.

        Keyword Arguments:
        game -- dictionary
        """
        # Initialise array for team types
        teamTypes = ["hTeam", "vTeam"]
        # Initialise object to hold scoreline of each team
        scoreline = {}
        for item in teamTypes:
            scoreline[item] = []
        # Iterate over all team types
        for team in teamTypes:
            for score in game[team]["linescore"]:
                scoreline[team].append(score["score"])
            # Append final score
            scoreline[team].append(game["hTeam"]["score"])
        # Return scoreline
        return scoreline

    # Function to extract game title and subtitle
    def extractGameTitle(self, game):
        """Genrate title and subtitle strings based on game.

        Keyword Arguments:
        game -- dictionary
        """
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
        # Return title and subtitle
        return {
            "title": title,
            "subtitle": subtitle
        }

    # Function to extract game status
    def extractGameStatus(self, game):
        """Generate status of game based on game clock.

        Keyword Arguments:
        game -- dictionary
        """
        # Initialise status string
        status = ""
        # Set clock based on status of game
        if game["statusNum"] == 1:
            # Calculate hours to game start
            startTime = dateutil.parser.isoparse(game["startTimeUTC"]).replace(tzinfo=None)
            currentTime = datetime.now()
            # Set clock based on time to start
            if startTime - currentTime < timedelta(seconds=3600):
                diff = startTime.minute - currentTime.minute
                status = "Starts in "+str( diff if diff > 0 else (60+diff) )+" mins"
            else:
                diff = startTime.hour - currentTime.hour
                status = "Starts in "+str( diff if diff > 0 else (24+diff) )+" hrs"
        elif game["statusNum"] == 2:
            status = game["clock"]
        else:
            status = "FINAL"

    # Function to extract game data
    def extractGameData(self, scoreboard):
        """Extract essential game data from scoreboard.

        Keyword Arguments:
        scoreboard -- dictionary
        """
        # Initialise array to hold games
        gameList = []
        # Iterate over games
        for game in scoreboard["games"]:
            # Call function to get game title and subtitle
            titleObj = self.extractGameTitle(game)

            # Call function to get game scoreline
            scorelineObj = self.extractGameScoreline(game)

            # Call function to get game status
            clock = self.extractGameStatus(game)

            # Append game data to array
            gameList.append({
                "gameId": game["gameId"],
                "boxscoreURL": "https://global.nba.com/boxscore/#!/"+str(game["gameId"]),
                "title": titleObj["title"],
                "subtitle": titleObj["subtitle"],
                "clock": clock,
                "hTeam": {
                    "id": game["hTeam"]["teamId"],
                    "triCode": game["hTeam"]["triCode"],
                    "score": scorelineObj["hTeam"]
                },
                "vTeam": {
                    "id": game["vTeam"]["teamId"],
                    "triCode": game["vTeam"]["triCode"],
                    "score": scorelineObj["vTeam"]
                }
            })
        # Return game list
        return gameList


    # Function to get current date
    def getCurrentDate(self):
        """Return current date from links."""
        # Initialise variabe for date
        date = ""
        # Check if links is populated
        if len(self.links.keys()) > 0:
            date = self.links["links"]["currentDate"]
        # Return date
        return date

    # Function to return URL for standings
    def getStandingsURL(self):
        """Return URL to site with team standings."""
        return "https://www.nba.com/standings"

    # Function to get today score
    def getScoreToday(self):
        """Call function to get score and pass current date to it."""
        return self.getScoreByDay(self.getCurrentDate())

    # Function to get score by date
    def getScoreByDay(self, date):
        """Send a request to get list of games and their details on a particular day.

        Keyword Arguments:
        date -- string (YYYYMMDD)
        """
        # Initialise array to hold result
        result = []
        # Check if links is populated
        if len(self.links.keys()) > 0:
            # Send request
            res = self.sender["JSON"](self.baseURL+self.links["links"]["scoreboard"].replace("{{gameDate}}", date))
            # Check response status
            if res["status"] == 200:
                # Call function to extract game data
                result = self.extractGameData(res["payload"])
        # Return result array
        return result
