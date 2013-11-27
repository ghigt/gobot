from unittest import TestCase
from AdminBot.Bot.Adress.AdressBase import AdressBase
from AdminBot.Bot import settings

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


class TestAdressBase(TestCase):
    def setUp(self):
        self.adresse = AdressBase(settings.HTTP_MODE,
                                  settings.API_KEY_BETASERIE, "://test")

    def test_get_http(self):
        self.assertEqual(self.adresse.get_http(), "https", "")

    def test_set_http(self):
        self.adresse.set_http("HTTP")
        self.assertEqual(self.adresse.http, "HTTP", "")

    def test_get_api_key(self):
        self.assertEqual(self.adresse.get_api_key(),
                         settings.API_KEY_BETASERIE, "")

    def test_set_api_key(self):
        self.adresse.set_api_key("test")
        self.assertEqual(self.adresse.api_key, "test", "")

    def test_get_adress(self):
        self.assertEqual(self.adresse.get_adress(), "://test", "")

    def test_set_adress(self):
        self.adresse.set_adress("://Je suis un test")
        self.assertEqual(self.adresse.address, "://Je suis un test", "")
