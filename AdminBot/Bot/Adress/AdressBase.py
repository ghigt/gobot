__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

from abc import abstractmethod
from AdminBot.Bot import settings


class AdressBase(object):
    """Adress base for the other adress object
    you must use for other bot."""

    def __init__(self, http=settings.HTTP_MODE, api_key=None, address=None):
        self.http = http
        self.api_key = api_key
        self.address = address

    def set_http(self, http=settings.HTTP_MODE):
        self.http = http.lower()

    def get_http(self):
        return self.http

    def set_api_key(self, api_key=None):
        self.api_key = api_key

    def get_api_key(self):
        return self.api_key

    def set_adress(self, address=None):
        self.address = address

    def get_adresse(self):
        return self.address

    @abstractmethod
    def get_new_address(self):
        raise NotImplementedError("Subclasses Should have implemented this")

    @abstractmethod
    def get_new_address_with_all_param(self, api_key, address, http=settings.HTTP_MODE):
        raise NotImplementedError("Subclasses Should have implemented this")