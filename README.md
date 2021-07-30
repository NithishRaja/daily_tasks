# AUTOMATE DAILY TASKS

A simple program to get the "international day", a random quote, a song, calendar events and NBA scores

## Editing code

* Main logic beings at `src/main.py`
* To get an overview of the program, visit `src/compose/composer.py`
* Each functionality is separated into a separate package and placed inside `src` directory

## Running code

* Install python dependencies by running `pip install -r requirements.txt`
* Install javascript dependencies by running `npm install`
* Run `python src/main.py` to run the program
* Visit `localhost:8000` to view the UI

### Calendar

* Create a directory called `userData` in root path
* Place ics file inside `userData` directory
* Update ics file name in `config.json` file

### Configuration

* Calender filename needs to be specified in `config.json` file
* Config file should have the format specified below
```
{
  "calendar": {
    "fileName": <file name>
  }
}
```

### Credentials

* Youtube data api key and twitter bearer token are required
* Credentials need to be placed inside `credentials.json` file in the format depicted below
```
{
  "twitter": {
    "BearerToken": <token>
  },
  "youtube": {
    "APIKey": <key>
  }
}
```

# Docker

* The docker image can be found at [docker hub](https://hub.docker.com/repository/docker/nithishraja/start-day)
* Instructions on how to use the image are also at [docker hub](https://hub.docker.com/repository/docker/nithishraja/start-day)
