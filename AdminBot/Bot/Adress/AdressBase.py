__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

from abc import abstractmethod
from AdminBot.Bot import settings


class AdressBase():
    """Adress base for the other adress object
    you must use for other bot."""
    http = None
    api_key = None
    address = None

    def __init__(self, http=settings.HTTP_MODE, api_key=None, address=None):
        self.http = http
        self.api_key = api_key
        self.address = address

    def get_http(self):
        """
        Return the value of http attribute
        @return: http attribute, str()
        """
        return self.http

    def set_http(self, http=settings.HTTP_MODE):
        """
        HTTP attribute, can be http, or https
        Setter for http attribute
        @param http: http or https
        """
        self.http = http

    def get_api_key(self):
        """
        Api Key attribute, allows authenticate bot on different Api.
        Return value of api_key attribute
        @return: str() api_key
        """
        return self.api_key

    def set_api_key(self, api_key=None):
        """
        Api Key attribute, allows authenticate bot on different Api.
        Setter for api_key attribute
        @param api_key: None by default
        """
        self.api_key = api_key

    def get_adress(self):
        """
        Adresse attribute to made the request
        Return value of adresse attribute
        @return: str() with adresse
        """
        return self.address

    def set_adress(self, address=None):
        """
        Setter adresse attribute to made the request
        @param address: None by default
        """
        self.address = address

    @abstractmethod
    def get_new_address(self):
        raise NotImplementedError("Subclasses Should have implemented this")

    @abstractmethod
    def get_new_address_with_all_param(self, api_key, address, http=settings.HTTP_MODE):
        raise NotImplementedError("Subclasses Should have implemented this")

    http = property(get_http, set_http)
    api_key = property(get_api_key, set_api_key)
    address = property(get_adress, set_adress)