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
import threading
import os
from django.core.management import setup_environ
import settings

#For Alexandre
sys.path.append('/home/nkio/PycharmProjects/DjangoBot/AdminBot/')
#For serveur
#sys.path.append(os.path.join(os.path.abspath('..'), '../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoBot.settings'

setup_environ(settings)
from Connexion import Connexion
from AdminBot.models import Episode, Show


class Betaseries:
    logging.config.fileConfig("../configuration.cfg")
    log = logging.getLogger("BetaSeries")

    def __init__(self):
        self.list_url = self.get_info_for_each_episode()

    @staticmethod
    def get_api_key():
        return settings.API_KEY_BETASERIE

    @staticmethod
    def get_logger(self):
        return self.log

    def get_url_for_each_serie(self):
        """
        Permet d'avoir toute les URL des series
        :return List() url:
        """
        listurl = []
        listtmp = Connexion('http').getAllShow()
        for clef in listtmp.values():
            listurl.append(clef['url'])
        self.log.info("Récupération des URL fini")
        return listurl

    def get_id_for_each_show(self):
        """
        Permet d'avoir tout les ID des series
        :return List() ID:
        """
        listid = []
        listtmp = Connexion('http').getAllShow()
        for clef in listtmp:
            listid.append(clef)
        self.log.info("Récupération des iD fini")
        return listid

    def get_info_for_each_show(self):
        """
        Lit le Json reçu des show
        et créer un objet qui est ensuite stocké en base
        """
        ids = self.get_id_for_each_show()
        for idShow in ids:
            show = Connexion('http').getEachShow(idShow)
            if show != False:
                self.deserialase_show(show)
                self.log.info("Création d'un show")

    def get_info_for_each_episode(self):
        """
        Lit le Json reçu des episodes
        et créer un objet qui est ensuite stocké en base
        """
        ids = self.get_id_for_each_show()
        for idShow in ids:
            episode = Connexion('http').getEpisodeFromIDShow(idShow)
            if episode != False:
                self.deserialase_episode(episode)
                self.log.info("Création des épisode pour la série %s" % str(idShow))

    @staticmethod
    def deserialase_show(self, obj):
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
            return p
        else:
            self.log.error("Erreur à la déserialisation")

    @staticmethod
    def deserialase_episode(self, objs):
        show = None
        for obj in objs:
            try:
                show = Show.objects.get(title=obj['show_title'], idbetaserie=obj['show_id'])
            except Show.DoesNotExist:
                self.deserialase_show(Connexion('http').getEachShow(obj['show_id']))
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