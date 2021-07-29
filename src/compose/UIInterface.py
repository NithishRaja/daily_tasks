#
# File containing abstract class for UI interface
#
#

# Dependencies
from abc import ABC, abstractmethod

# The class should always contain beginDisplay and endDisplay function
# beginDisplay function should initiate the user interface
# endDisplay function should stop functioning of the user interface
# In case of errors/failures, throw the error and exit

# Initialise class
class UIInterface(ABC):

    @abstractmethod
    def beginDisplay(self):
        pass

    @abstractmethod
    def endDisplay(self):
        pass
