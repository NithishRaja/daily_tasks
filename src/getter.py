#
# File containing code for abstract getter class
#
#

# Dependencies
from abc import ABC, abstractmethod

# Initialise getter class
class Getter(ABC):

    @abstractmethod
    def getData(self):
        pass
