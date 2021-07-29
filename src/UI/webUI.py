#
# File containing code for web ui class
#
#

# Dependencies
import threading, json
from subprocess import Popen, PIPE

# Local Dependencies
from compose.UIInterface import UIInterface
from compose.persistenceInterface import PersistenceInterface

# Initialise class
class WebUI(UIInterface):
    # Initialise constructor
    def __init__(self, persistence: PersistenceInterface):
        # Initialise persistence object
        self.persistence = persistence
        # Initialise variable to hold server process
        self.server = None

    # Function to start server
    def startServer(self):
        """Create a subprocess and run the server using it."""
        # Start server as a subprocess
        self.server = Popen(["node", "server/server.js"], stdin=PIPE)
        # Initialise dictionary to hold data
        data = {}
        # Iterate over keys
        for item in ["song", "event", "quote", "score", "day", "word"]:
            #  Retrieve data from persistence object
            data[item] = self.persistence.retrieveDataByKey(item)
        # print("python", json.dumps(data))
        # Send data to server
        self.server.communicate(input=json.dumps(data).encode())

    # Function to start display
    def beginDisplay(self):
        """Create a thread and use the thread to call start server."""
        # Initialise thread
        serverThread = threading.Thread(target=self.startServer)
        # Start thread
        serverThread.start()

    # Function to stop display
    def endDisplay(self):
        """Call kill function on subprocess."""
        # Close input stream of subprocess
        self.server.stdin.close()
        # Kill subprocess
        self.server.kill()
        # Wait till subprocess has terminated
        self.server.wait()
