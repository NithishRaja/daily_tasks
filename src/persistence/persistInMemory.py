#
# File containing persist in memory class
#
#

# Dependencies

# Local Dependencies
from compose.persistenceInterface import PersistenceInterface

# Initialise class
class PersistInMemory(PersistenceInterface):
    # Initialise constructor
    def __init__(self):
        # Initialise dictionary to hold data
        self.data = {}

    # Function to store data
    def persistDataByKey(self, key, data):
        """Store given data with its key.

        Keyword Arguments:
        key -- string
        data -- dictionary
        """
        self.data[key] = data

    # Function to fetch data
    def retrieveDataByKey(self, key):
        """Search for data by its key and return it.

        Keyword Arguments:
        key -- string
        """
        # Initialise variable for data
        data = None
        # Check if key exists
        if key in self.data.keys():
            data = self.data[key]
        # Return data
        return data
