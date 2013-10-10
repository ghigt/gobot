# -*- coding: utf-8 -*-

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import settings
import logging
import requests


class Connexion:
    log = logging.getLogger("BetaSeries")
    header = {'Accept': 'application/json', 'user-agent': settings.NAMEPROJECT}

    def __init__(self, httpType='http'):
        self.httpType = httpType

    def getAllShow(self):
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