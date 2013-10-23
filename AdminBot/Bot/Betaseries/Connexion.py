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
from AdminBot.Bot.Adress.AdressBetaSeries import AdressBetaseries


class Connexion:
    access_url = ((0, '://api.betaseries.com/shows/display/all.json?key='),
                  (1, '://api.betaseries.com/shows/display?key='),
                  (2, '://api.betaseries.com/shows/episodes?key=%s&id=%s'))

    log = logging.getLogger("BetaSeries")
    header = {'Accept': 'application/json', 'user-agent': settings.NAMEPROJECT}

    def __init__(self, http_type='http'):
        self.http_type = http_type
        self.adress = AdressBetaseries(http_type, settings.API_KEY_BETASERIE)

    def get_all_show(self):
        self.adress.set_adress(self.access_url[0][1])
        r = requests.get(self.adress.get_new_address(), headers=self.header)
        self.log.info("Adresse interrogée = %s" % self.adress.get_new_address())
        if r.status_code == requests.codes.ok:
            self.log.info("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            return r.json()['root']['shows']
        else:
            self.log.error("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            r.raise_for_status()
            return False

    def get_each_show(self, id_show):
        self.adress.set_adress(self.access_url[1][1])
        print self.adress.get_new_address() + "&id=%s" % id_show
        r = requests.get(self.adress.get_new_address() + "&id=%s" % id_show, headers=self.header)
        self.log.info("Adresse interrogée = %s" % str(self.adress.get_new_address() + "&id=%s" % id_show))
        if r.status_code == requests.codes.ok:
            self.log.info("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            self.log.info("Récupération de la série  = %s" % str(id_show))
            try:
                r.json()
            except ValueError:
                self.log.error("Erreur sur le décodage du jSon, pass error")
                pass
            else:
                return r.json()
        else:
            self.log.error("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            return False

    def get_episode_from_id_show(self, id_show):
        self.adress.set_adress(self.access_url[2][1])
        r = requests.get(self.adress.get_new_address() + "&id=%s" % id_show, headers=self.header)
        self.log.info("Adresse interrogée = %s" % str(self.adress.get_new_address() + "&id=%s" % id_show))
        if r.status_code == requests.codes.ok:
            self.log.info("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            self.log.info("Récupération des épisodes de la série  = %s" % str(id_show))
            try:
                r.json()['episodes']
            except ValueError:
                self.log.error("Erreur sur le décodage du jSon, pass error")
                pass
            else:
                return r.json()['episodes']
        else:
            self.log.error("Connexion à BetaSeries : Status de la page = %d" % r.status_code)
            return False

Connexion().get_each_show("222")
