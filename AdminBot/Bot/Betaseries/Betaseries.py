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

import sys, threading
import os
from datetime import *
sys.path.append('/home/nkio/PycharmProjects/DjangoBot/AdminBot/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoBot.settings'

from django.core.management import setup_environ
import settings

setup_environ(settings)
from Connexion import Connexion
from django.conf import settings
from django.db import models
from AdminBot.models import Episode, Show


class Betaseries:
    logging.config.fileConfig("../configuration.cfg")
    log = logging.getLogger("BetaSeries")

    def __init__(self):
        self.listURL = self.getInfoForEachShow()

    def __del__(self):
        None

    def get_API_key(self):
        return settings.API_KEY_BETASERIE

    def get_logger(self):
        return self.log

    def getUrlForEachSerie(self):
        """
        Permet d'avoir toute les URL des series
        :return List() url:
        """
        listUrl = []
        self.list = Connexion('http').getAllShow()
        for clef in self.list.values():
            listUrl.append(clef['url'])
        self.log.info("Récupération des URL fini")
        return listUrl

    def getIDForEachShow(self):
        """
        Permet d'avoir tout les ID des series
        :return List() ID:
        """
        listid = []
        self.list = Connexion('http').getAllShow()
        for clef in self.list:
            listid.append(clef)
        self.log.info("Récupération des iD fini")
        return listid

    def getInfoForEachShow(self):
        ids = self.getIDForEachShow()
        for idShow in ids:
            show = Connexion('http').getEachShow(idShow)
            if show != False:
                p = self.deserialaseShow(show)
                self.log.info("Création d'un show")

    def getInfoForEachEpisode(self):
        ids = self.getIDForEachShow()
        for idShow in ids:
            episode = Connexion('http').getEpisodeFromIDShow(idShow)
            if episode != False:
                self.deserialaseEpisode(episode)
                self.log.info("Création des épisode pour la série %s" % str(idShow))

    def deserialaseShow(self, obj):
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
                     language=obj['language'])
            try:
                x = Show.objects.get(title=obj['title'], creation=obj['creation'])
            except Show.DoesNotExist:
                p.save()
                a.start()
                self.log.info("Objet Save")
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
                         language=obj['language'])
                p.save()
                self.log.info("Objet Update")
            return p
        else:
            self.log.error("Erreur à la déserialisation")

    def deserialaseEpisode(self, objs):
        listEpisode = list()
        for obj in objs:
            ep = Episode(title=obj['title'],
                         season=obj['season'],
                         episode=obj['episode'],
                         showid=obj['show_id'],
                         show_title=obj['show_title'],
                         code=obj['code'],
                         description=obj['description'],
                         date=obj['date'])
            ep.save()
            listEpisode.append(ep)
        return listEpisode

Betaseries()