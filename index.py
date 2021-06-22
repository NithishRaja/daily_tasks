#
# Index File
#
#

# Dependencies
import threading
# Local dependencies
from src.app import App

app = App()

# Initialise threads
dayThread = threading.Thread(target=app.day, args=[])
quoteThread = threading.Thread(target=app.quote, args=[])
songThread = threading.Thread(target=app.song, args=[])
scoreThread = threading.Thread(target=app.score, args=[])
eventsThread = threading.Thread(target=app.events, args=[])

# Start threads
dayThread.start()
quoteThread.start()
songThread.start()
scoreThread.start()
eventsThread.start()

# app.start()
