#
# File containing code for abstract getter class
#
#

# Dependencies
from abc import ABC, abstractmethod

# Initialise getter class
class GetterInterface(ABC):

    @abstractmethod
    def getData(self):
        pass
