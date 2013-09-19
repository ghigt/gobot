# -*- coding: utf-8 -*-

__author__ = 'Alexandre Cloquet'

import settings
import logging
import requests


class Connexion:
    log = logging.getLogger("BetaSeries")
    header = {'Accept': 'application/json', 'user-agent': settings.NAMEPROJECT}

    def __init__(self, httpType='http'):
        self.httpType = httpType
        init = None

    def getAllShow(self):
        listp = []
        if self.httpType == 'http':
            settings.HTTP = 'http'
        else:
            settings.HTTP = 'https'
        adress = '%s://api.betaseries.com/shows/display/all.json?key=%s' % (settings.HTTP, settings.API_KEY_BETASERIE)
        r = requests.get(adress, headers=self.header)
        self.log.info("Adresse interrogeée = %s" % adress)
        if r.status_code == requests.codes.ok:
            self.log.info("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            return r.json()['root']['shows']
        else:
            self.log.error("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            r.raise_for_status()
            return False

    def getEachShow(self, idShow):
        if self.httpType == 'http':
            settings.HTTP = 'http'
        else:
            settings.HTTP = 'https'
        adress = '%s://api.betaseries.com/shows/display?key=%s&id=%s' % (settings.HTTP, settings.API_KEY_BETASERIE, idShow)
        r = requests.get(adress, headers=self.header)
        self.log.info("Adresse interrogeée = %s" % str(adress))
        if r.status_code == requests.codes.ok:
            self.log.info("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            self.log.info("Récupération de la série  = %s" % str(idShow))
            return r.json()
        else:
            self.log.error("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            return False

    def getEpisodeFromIDShow(self, idShow):
        if self.httpType == 'http':
            settings.HTTP = 'http'
        else:
            settings.HTTP = 'https'
        adress = '%s://api.betaseries.com/shows/episodes?key=%s&id=%s' % (settings.HTTP, settings.API_KEY_BETASERIE, idShow)
        r = requests.get(adress, headers=self.header)
        self.log.info("Adresse interrogeée = %s" % str(adress))
        if r.status_code == requests.codes.ok:
            self.log.info("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            self.log.info("Récupération des épisodes de la série  = %s" % str(idShow))
            return r.json()['episodes']
        else:
            self.log.error("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            return False

