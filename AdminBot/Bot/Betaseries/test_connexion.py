from unittest import TestCase
from Betaseries import Connexion
from mock import *
import time
import requests
from requests.exceptions import *

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


class TestConnexion(TestCase):
    def setUp(self):
        self.all_show = Connexion().get_all_show()
        self.show = Connexion().get_each_show("222")
        self.episodes = Connexion().get_episode_from_id_show("666")
        time.sleep(90)

    def test_get_all_show(self):
        assert self.all_show == Connexion().get_all_show()

    def test_get_each_show(self):
        assert self.show == Connexion().get_each_show("222")
        assert self.show != Connexion().get_each_show("223")
        assert self.show != Connexion().get_each_show("500")
        assert self.show != Connexion().get_each_show("560")
        assert self.show != Connexion().get_each_show("-1")

    def test_get_episode_from_id_show(self):
        assert self.episodes == Connexion().get_episode_from_id_show("666")
        assert self.episodes != Connexion().get_episode_from_id_show("667")
        assert self.episodes != Connexion().get_episode_from_id_show("668")
