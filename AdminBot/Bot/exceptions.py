__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

__all__ = {"InvalidInfoBot", "IdAlreadyUse"}


class InvalidInfoBot(Exception):
    """Invalid information from Bot"""


class IdAlreadyUse(Exception):
    """Id already use in database"""


class NoRespondFromAPI(Exception):
    """Api don't respond"""