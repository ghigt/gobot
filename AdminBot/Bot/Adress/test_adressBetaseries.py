from unittest import TestCase
from AdressBase import AdressBase
from AdressBetaSeries import AdressBetaseries
from AdminBot.Bot import settings

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


class TestAdressBetaseries(TestCase):
    def setUp(self):
        self.adressbeta = AdressBetaseries(settings.HTTP_MODE, settings.API_KEY_BETASERIE, "://test")

    def test_get_new_address(self):
        self.assertEqual(self.adressbeta.get_new_address(), "https://test3e803b0b5556")

    def test_get_new_address_with_all_param(self):
        self.assertEqual(self.adressbeta.get_new_address_with_all_param(
            settings.API_KEY_BETASERIE,"://test", settings.HTTP_MODE), "https://test3e803b0b5556")