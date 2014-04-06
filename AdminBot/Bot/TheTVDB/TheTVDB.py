
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
from AdminBot.models import Show, Episode


class TheTVDB():#BotBase):
    http_type = "http"
    base_url = "://thetvdb.com/index.php"
    show_url = "?tab=series&id="
    season_url = "?tab=season"
    episode_url = "?tab=episode"
    seriesid_url = "&seriesid="
    seasonid_url = "&seasonid="
    id_url = "&id="
    headers = {'User-Agent' : 'Chrome/16.0'}
    logging.config.fileConfig(settingBot.CONFIG_LOG)
    log = logging.getLogger("TheTVDB")

    def __init__(self):
        self.register_bot()
        self.get_all_series()

    def register_bot(self):
        """
        Allow to register TheTVDB Bot in database
        """
        bot = RegisterBot(version=0.01, actif=True,
                          log_bot="TheTVDBLogInfo.log",
                          error_bot="THETVDBLogError.log",
                          name="TheTVDB",
                          nb_iter=0, last_use=datetime.datetime.today())

    def get_all_series(self):
        """
        Get a text response for the search for series in TheTVDB and call 
        the method deserialise_serie to set them in the database
        :return: nothing
        """
        i = 1
        try:
            while i:
                
                r = requests.get(self.http_type + self.base_url + self.show_url + str(i), headers=self.headers)

                if r.status_code == requests.codes.ok:
                    self.log.info("Connexion à TheTVDB : "
                                  "Status de la page = %d" % r.status_code)
                print(r.text)
                i += 1
                # if series valid:
                # check_seasons()
                # deserialise_serie()
        except:
            self.log.error("Erreur durant la récupération des données.")
        return

    def check_seasons(self):
        """
        Check the number of seasons of the serie. For each season, call the 
        method get_all_episodes with the seasonid
        :return: true if a season is found else return false
        """
        flag = false
        while ():
            get_all_episodes(seasonid)
            flag = true
        return flag

    def get_all_episodes(self, seasonid):
        """
        Get a text response for the search for episodes in TheTVDB and call 
        the method deserialase_episode to set them in the database
        :return: nothing
        """
        i = 1
        try:
            r_season = requests.get(self.http_type + self.base_url + self.season_url + self.seriesid_url + seriesid + self.seasonid_url + seasonid, headers=self.headers)
            while i <= ord('z'):
                
                r_season = requests.get(self.http_type + self.base_url + self.episode_url + self.seriesid_url + seriesid + self.seasonid_url + seasonid + self.id_url + id_episode, headers=self.headers)

                if r.status_code == requests.codes.ok:
                    self.log.info("Connexion à TheTVDB : "
                                  "Status de la page = %d" % r.status_code)
                print(r.text)
                #self.deserialase_episode(r.text())
                i += 1
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

    def deserialase_serie(self, obj):
        """
        Extract all data from the object and made an anime object
        for Database
        :see: AdminBot/model.py
        :param self: itself
        :return: Nothing in all case
        """
        return

    def deserialase_episode(self, obj):
        return

    def get_method(self):
        """
        Allows to have all method from the bot

        :return: List of all method
        """
        return 'register_bot', 'get_all_series', 'check_seasons', \
               'get_all_episodes', 'get_logger', 'deserialase_serie', \
               'deserialase_episode'

if __name__ == '__main__':
    TheTVDB()
