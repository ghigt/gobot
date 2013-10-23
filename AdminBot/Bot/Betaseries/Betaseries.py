# -*- coding: utf-8 -*-

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import logging
import re
import logging.config
import sys
import os
from django.core.management import setup_environ
import settings

#For Alexandre
sys.path.append('/home/nkio/PycharmProjects/DjangoBot/AdminBot/')
#For server
#sys.path.append(os.path.join(os.path.abspath('..'), '../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoBot.settings'

setup_environ(settings)
from Connexion import Connexion
from AdminBot.models import Episode, Show


class Betaseries:
    logging.config.fileConfig("../configuration.cfg")
    log = logging.getLogger("BetaSeries")

    def __init__(self):
        self.get_info_for_each_episode()

    @staticmethod
    def get_api_key():
        """
        Static Method
        Allows to have API key for Betaserie API
        @return: str() with API key
        """
        return settings.API_KEY_BETASERIE

    @staticmethod
    def get_logger(self):
        """
        Static Method
        Allows to have the logger for Betaserie API
        @return: Logger
        """
        return self.log

    def get_url_for_each_series(self):
        """
        Allows to have all url series for Betaserie API
        @return: List(url) for every series
        """
        list_url = []
        list_tmp = Connexion('http').get_all_show()
        for clef in list_tmp.values():
            list_url.append(clef['url'])
        self.log.info("Récupération des URL fini")
        return list_url

    def get_id_for_each_show(self):
        """
        Allows to have all id series for Betaserie API
        @return: List(id) for every series
        """
        list_id = []
        list_tmp = Connexion('http').get_all_show()
        for clef in list_tmp:
            list_id.append(clef)
        self.log.info("Récupération des iD fini")
        return list_id

    def get_info_for_each_show(self):
        """
        Get the Json file from series, and
        make an object for ORM Django
        """
        ids = self.get_id_for_each_show()
        for idShow in ids:
            show = Connexion('http').get_each_show(idShow)
            if show != False:
                self.deserialase_show(show)
                self.log.info("Création d'un show")

    def get_info_for_each_episode(self):
        """
        Get the Json file from episode, and
        make an object for ORM Django
        """
        ids = self.get_id_for_each_show()
        for idShow in ids:
            episode = Connexion('http').get_episode_from_id_show(idShow)
            if episode != False:
                self.deserialase_episode(episode)
                self.log.info("Création des épisode pour la série %s" % str(idShow))

    def deserialase_show(self, obj):
        """
        Extract all data from the object and made an Show object
        for Database
        @see: AdminBot/model.py
        @param self: itself
        @param obj: object from Json file from Betaserie API
        """
        if 'show' in obj:
            obj = obj['show']
            if len(obj['genres']) == 0:
                obj['genres'] = "  "
            p = Show(thetvdb_id=obj['thetvdb_id'],
                     imdb_id=obj['imdb_id'],
                     title=obj['title'],
                     description=re.escape(obj['description']),
                     seasons=obj['seasons'],
                     nbepisode=obj['episodes'],
                     follower=obj['followers'],
                     comment=obj['comments'],
                     similars=obj['similars'],
                     characters=obj['characters'],
                     creation=obj['creation'],
                     genre=obj['genres'][0],
                     lenght=obj['length'],
                     status=obj['status'],
                     language=obj['language'],
                     idbetaserie=obj['id'])
            try:
                x = Show.objects.get(title=obj['title'], creation=obj['creation'])
            except Show.DoesNotExist:
                p.save()
                self.log.info("Show Save")
            else:
                p = Show(id=x.id,
                         thetvdb_id=obj['thetvdb_id'],
                         imdb_id=obj['imdb_id'],
                         title=obj['title'],
                         description=obj['description'],
                         seasons=obj['seasons'],
                         nbepisode=obj['episodes'],
                         follower=obj['followers'],
                         comment=obj['comments'],
                         similars=obj['similars'],
                         characters=obj['characters'],
                         creation=obj['creation'],
                         genre=obj['genres'][0],
                         lenght=obj['length'],
                         status=obj['status'],
                         language=obj['language'],
                         idbetaserie=obj['id'])
                p.save()
                self.log.info("Show Update")
        else:
            self.log.error("Erreur à la déserialisation")

    def deserialase_episode(self, objs):
        """
        Extract all data from the object and made an Episode object
        for Database
        @see: AdminBot/model.py
        @param self: itself
        @param objs: object from Json file from Betaserie API
        """
        show = None
        for obj in objs:
            try:
                show = Show.objects.get(title=obj['show_title'], idbetaserie=obj['show_id'])
            except Show.DoesNotExist:
                self.deserialase_show(Connexion('http').get_each_show(obj['show_id']))
            else:
                show = Show.objects.get(title=obj['show_title'], idbetaserie=obj['show_id'])
            ep = Episode(title=obj['title'],
                         season=obj['season'],
                         episode=obj['episode'],
                         showid=obj['show_id'],
                         show_title=obj['show_title'],
                         code=obj['code'],
                         description=obj['description'],
                         date=obj['date'])
            ep.show_id = show.id
            try:
                x = Episode.objects.get(title=obj['title'], show_title=obj['show_title'])
            except Episode.DoesNotExist:
                ep.save()
                self.log.info("Episode Save")
            else:
                ep = Episode(id=x.id,
                             title=obj['title'],
                             season=obj['season'],
                             episode=obj['episode'],
                             showid=obj['show_id'],
                             show_title=obj['show_title'],
                             code=obj['code'],
                             description=obj['description'],
                             date=obj['date'])
                ep.show_id = show.id
                ep.save()
                self.log.info("Episode Update")

Betaseries()