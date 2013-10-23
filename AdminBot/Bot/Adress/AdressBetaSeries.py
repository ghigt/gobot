__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

from AdminBot.Bot import settings
from AdressBase import AdressBase


class AdressBetaseries(AdressBase):
    def __init__(self, http=None, api_key=None, address=None):
        AdressBase.__init__(self, http, api_key, address)

    def get_new_address(self):
        """
        Format new address to make a request http on it
        @return: str() New address formated @raise KeyError: http not set, adress not set, api_key not set
        """
        if self.http is None or self.address is None or self.api_key is None:
            raise KeyError("You must use get_new_adress_with_all_param")
        return '%s%s%s' % (self.http, self.address, self.api_key)

    def get_new_address_with_all_param(self, api_key, address, http=settings.HTTP):
        """
        Format new adress to make a request http on it with all parameters
        @param api_key: Need an Api key to login on server
        @param address: Need address to make a request
        @param http: Need http or https
        @return: str() New address formated
        """
        return '%s%s%s' % (http, address, api_key)