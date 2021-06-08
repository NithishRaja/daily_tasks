# AUTOMATE DAILY TASKS

A simple program to get the "international day", a random quote and a song

## Editing code

* Main logic beings at `index.py`
* Different functionality is separated into separate files located inside `src/` directory

## Running code

* Run `python index.py` to run the program
* Data retrieved is stored inside `data/` directory

### Configuration

* The expiry time for cache can be set in `config.json`
* Expiry time should adhere to this format `[<days>, <seconds>, <microseconds>]`
* Number of tweets retrieved can be altered in `config.json`
* Number of tweets should always be between 1 to 10
