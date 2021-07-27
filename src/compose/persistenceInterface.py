#
# File containing code for persistence interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain a persistDataByKey and retrieveDataByKey function
# persistDataByKey function takes key (string) and data (JSON) as input
# retrieveDataByKey function takes key (string) as input
# retrieveDataByKey should return JSON matching the given key
# In case data for given key doesn't exist, return None

# Initialise class
class PersistenceInterface(ABC):

    @abstractmethod
    def persistDataByKey(self, key, data):
        pass

    @abstractmethod
    def retrieveDataByKey(self, key):
        pass
