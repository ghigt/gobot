
# -*- coding: utf-8 -*-

__author__ = 'Alain Cariou'
__credits__ = ["Alain Cariou"]
__version__ = "0.1"
__maintainer__ = "Alain Cariou"
__email__ = "alaincariou.p@gmail.com"
__status__ = "Development"

import logging
import logging.config
import sys
import os
#from django.core.management import setup_environ
import settings
import requests
import time

#For Alexandre

#sys.path.append('/home/nkio/PycharmProjects/DjangoBot/AdminBot/')
#sys.path.append("C:/Users/Nkio/PycharmProjects/DjangoBot/AdminBot/")
##For server
##sys.path.append(os.path.join(os.path.abspath('..'), '../../'))
#os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoBot.settings'
#
#setup_environ(settings)

#For Alain

sys.path.append('/home/alaundo/bot/DjangoBot/AdminBot/')
sys.path.append(os.path.join(os.path.abspath('..'), '../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoBot.settings'

import datetime
from AdminBot.Bot import settings as settingBot
from AdminBot.Bot.RegisterBot.RegisterBot import RegisterBot
from AdminBot.Bot.bot.BotBase import BotBase
from AdminBot.models import Anime, Manga


class MyAnimeList():#BotBase):
    http_type = "http"
    base_url = "://myanimelist.net/"
    anime_url = "api/anime/"
    manga_url = "api/manga/"
    search_url = "search.xml?q="
    headers = {'User-Agent' : 'Chrome/16.0'}
    logging.config.fileConfig(settingBot.CONFIG_LOG)
    log = logging.getLogger("MyAnimeList")

    def __init__(self):
        self.register_bot()
        self.connect_to_api()
        self.get_all_anime()
        self.get_all_manga()

    def connect_to_api(self):
        r = requests.get("http://myanimelist.net/api/account/verify_credentials.xml", headers=self.headers, auth=(settings.LOGIN, settings.PASSWORD))

    def register_bot(self):
        """
        Allow to register MyAnimeList Bot in database
        """
        bot = RegisterBot(version=0.01, actif=True,
                          log_bot="MyAnimeListLogInfo.log",
                          error_bot="MyAnimeListLogError.log",
                          name="MyAnimeList",
                          nb_iter=0, last_use=datetime.datetime.today())

    def get_all_anime(self):
        """
        Get a text response for the search for anime in MyAnimeList and call 
        the method deserialise_anime to set them in the database
        :return: nothing
        """
        i = ord('a')
        
        try:
            while i <= ord('z'):
                
                r = requests.get(self.http_type + self.base_url + self.anime_url + self.search_url + str(chr(i)), headers=self.headers, auth=(settings.LOGIN, settings.PASSWORD))

                if r.status_code == requests.codes.ok:
                    self.log.info("Connexion à MyAnimeList : "
                                  "Status de la page = %d" % r.status_code)
                print(r.text)
                #self.deserialase_anime(r.text())
                i += 1
                time.sleep(settings.TIME_TO_WAIT)
        except:
            self.log.error("Erreur durant la récupération des données.")
        return

    def get_all_manga(self):
        """
        Get a text response for the search for manga in MyAnimeList and call 
        the method deserialise_manga to set them in the database
        :return: nothing
        """
        i = ord('a')
        
        try:
            while i <= ord('z'):
                
                r = requests.get(self.http_type + self.base_url + self.manga_url + self.search_url + str(chr(i)), headers=self.headers, auth=(settings.LOGIN, settings.PASSWORD))

                if r.status_code == requests.codes.ok:
                    self.log.info("Connexion à MyAnimeList : "
                                  "Status de la page = %d" % r.status_code)
                print(r.text)
                self.deserialase_manga(r.text())
                i += 1
                time.sleep(settings.TIME_TO_WAIT)
        except:
            self.log.error("Erreur durant la récupération des données.")
        return

    def get_logger(self):
        """
        Static Method
        Allows to have the logger for MyAnimeList API
        :return: Logger
        """
        return self.log

    def deserialase_anime(self, obj):
        """
        Extract all data from the object and made an anime object
        for Database
        :see: AdminBot/model.py
        :param self: itself
        :param obj: object from text content from MyAnimeList API
        :return: Nothing in all case
        """
        # Parser le contenu xml
        # Vérifier que l'enregistrement ne soit pas déjà dans la bdd
        # S'il ne l'est pas l'intégrer
        return

    def deserialase_manga(self, obj):
        return

    def get_method(self):
        """
        Allows to have all method from the bot

        :return: List of all method
        """
        return 'connect_to_api', 'register_bot', 'get_all_anime', \
               'get_all_manga', 'get_logger', 'deserialase_anime', \
               'deserialase_manga'

if __name__ == '__main__':
    MyAnimeList()
