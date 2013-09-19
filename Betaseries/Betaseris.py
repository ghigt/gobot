# -*- coding: utf-8 -*-


__author__ = 'Alexandre Cloquet'

import settings
import logging
import logging.config
import requests

from Connexion import Connexion
from Betaseries.ObjectDeserialised.Show import Show
from Betaseries.ObjectDeserialised.Episode import Episode


class Betaseries:
    logging.config.fileConfig("../configuration.cfg")
    log = logging.getLogger("BetaSeries")

    def __init__(self):
        init = None
        self.listURL = self.getInfoForEachEpisode()


    def __del__(self):
        init = None

    def get_API_key(self):
        return settings.API_KEY_BETASERIE

    def get_logger(self):
        return self.log

    def getUrlForEachSerie(self):
        """
        Permet d'avoir toute les URL des series
        :return Une liste d'URL:
        """
        listUrl = []
        self.list = Connexion('http').getAllShow()
        for clef in self.list.values():
            listUrl.append(clef['url'])
        self.log.info("Récupération des URL fini")
        return listUrl

    def getIDForEachShow(self):
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
                self.log.info("Création de l'objet %s" % p.title)

    def getInfoForEachEpisode(self):
        ids = self.getIDForEachShow()
        for idShow in ids:
            episode = Connexion('http').getEpisodeFromIDShow(idShow)
            if episode != False:
                p = self.deserialaseEpisode(episode)
                self.log.info("Création des épisode pour la série %s" % str(idShow))

    def deserialaseShow(self, obj):
        if 'show' in obj:
            obj = obj['show']
            return Show(obj['id'], obj['thetvdb_id'], obj['imdb_id'], obj['title'], obj['description'],
                        obj['seasons'], obj['episodes'], obj['followers'], obj['comments'], obj['similars'],
                        obj['characters'], obj['creation'], obj['genres'], obj['length'], obj['status'],
                        obj['language'])
        else:
            self.log.error("Erreur à la déserialisation")

    def deserialaseEpisode(self, objs):
        listEpisode = list()
        for obj in objs:
            ep = Episode(obj['id'], obj['title'], obj['season'], obj['episode'], obj['show_id'],
                        obj['show_title'], obj['code'], obj['description'], obj['date'])
            listEpisode.append(ep)
        return listEpisode

Betaseries()