
# -*- coding: utf-8 -*-

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import logging
import logging.config
import sys
import os
#from django.core.management import setup_environ
import settings
import requests

#For Alexandre

#sys.path.append('/home/nkio/PycharmProjects/DjangoBot/AdminBot/')
#sys.path.append("C:/Users/Nkio/PycharmProjects/DjangoBot/AdminBot/")
##For server
##sys.path.append(os.path.join(os.path.abspath('..'), '../../'))
#os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoBot.settings'
#
#setup_environ(settings)

# For Alain

sys.path.append('/home/alaundo/bot/DjangoBot/AdminBot/')
sys.path.append(os.path.join(os.path.abspath('..'), '../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoBot.settings'

import datetime
from AdminBot.Bot import settings as settingBot
from AdminBot.Bot.RegisterBot.RegisterBot import RegisterBot
from AdminBot.Bot.bot.BotBase import BotBase
from AdminBot.models import Music, Album, Track


class Deezer(BotBase):
    http_type = "http"
    base_url = "://api.deezer.com/";
    album_url = "album/";
    logging.config.fileConfig(settingBot.CONFIG_LOG)
    log = logging.getLogger("Deezer")

    def __init__(self):
        BotBase.__init__(self)
        #self.register_bot()
        self.get_url_for_all_album()

    def get_api_key(self):
        return super(Deezer, self).get_api_key()

    def get_info_for(self, value):
        return super(Deezer, self).get_info_for(value)

    def search(self, value):
        return super(Deezer, self).search(value)

    def register_bot(self):
        """
        Allow to register Deezer Bot in database
        """
        bot = RegisterBot(version=0.01, actif=True,
                          log_bot="DeezerLogInfo.log",
                          error_bot="DeezerLogError.log", name="Deezer",
                          nb_iter=0, last_use=datetime.datetime.today())

    def get_url_for_all_album(self):
        """
        Get a Json for each album in Deezer and call 
        the method deserialise_album to set them in the database
        :return: nothing
        """

        i = 2
        try:
            while 1:
                r = requests.get(self.http_type + self.base_url + self.album_url + str(i))
                if r.status_code == requests.codes.ok:
                    self.log.info("Connexion à Deezer : "
                                  "Status de la page = %d" % r.status_code)
                if r.text[2] != "e":
                    #print(str(r.json()["id"]) + ": " + r.json()["title"])
                    if str(r.json()["tracks"]["data"]) != "[]":
                        self.get_info_for_track_by_album(r.json())
                    self.deserialase_album(r.json())
                i += 1
        except:
            self.log.error("Erreur durant la récupération des données.")
        return

    def get_info_for_track_by_album(self, obj):
        """
        Call the method deserialase_music for each track in the album
        Call the method deserialase_track to link the music and the album
        :return: nothing
        """

        position = 1
        for track in obj["tracks"]["data"]:
            self.deserialase_music(track)
            self.deserialase_track(obj["id"], track["id"], position)
            position += 1
        return

    def get_logger(self):
        """
        Static Method
        Allows to have the logger for Deezer API
        :return: Logger
        """
        return self.log

    def deserialase_album(self, obj):
        """
        Extract all data from the object and made an Album object
        for Database
        :see: AdminBot/model.py
        :param self: itself
        :param obj: object from Json file from Deezer API
        :return: Nothing in all case
        """

        if "id" in obj:
            try:
                a = Album.objects.get(id_album=obj['id'],
                                      title=obj['title'],
                                      release_date=obj['release_date'])
                a.save()
                self.log.info("Album Update")
                return
            except Album.DoesNotExist:
                a = Album(id_album=obj['id'],
                          title=obj['title'],
                          link=obj['link'],
                          cover=obj['cover'],
                          nb_tracks=obj['nb_tracks'],
                          duration=obj['duration'],
                          fans=obj['fans'],
                          rating=obj['rating'],
                          release_date=obj['release_date'],
                          available=obj['available'],
                          artist=obj['artist'])
                a.save()
                self.log.info("Album Save")
        else:
            self.log.error("Erreur à la deserialisation")
        return

    def deserialase_music(self, obj):
        """
        Extract all data from the object and made an Music object
        for Database
        :see: AdminBot/model.py
        :param self: itself
        :param obj: object from Json file which contains the tracks of an album
        :return: Nothing in all case
        """

        try:
            m = Music.objects.get(id_music=obj['id'], title=obj['title'])
            m.save()
            self.log.info("Music Update")
            return
        except Music.DoesNotExist:
            m = Music(id_music=obj['id'],
                      title=obj['title'],
                      link=obj['link'],
                      duration=obj['duration'],
                      rank=obj['rank'],
                      preview_link=obj['preview'],
                      artist=obj['artist']['name'])
            m.show_id = self.show.id
            m.save()
            self.log.info("Music Save")
        else:
            self.log.error("Erreur à la deserialisation")
        return

    def deserialase_track(self, album_id, music_id, position):
        """
        Extract all data from the object and made a Track object
        for Database
        :see: AdminBot/model.py
        :param self: itself
        :param album_id: the id of the album containing the tracks
        :param music_id: the id of the track
        :param position: the position of the track in the album
        :return: Nothing in all case
        """

        try:
            t = Track.objects.get(album=album_id, music=music_id)
            t.save()
            self.log.info("Track Update")
            return
        except Music.DoesNotExist:
            t = Music(album=album_id,
                      music=music_id,
                      position=position)
            t.show_id = self.show.id
            t.save()
            self.log.info("Track Save")
        else:
            self.log.error("Erreur à la deserialisation")
        return

    def get_method(self):
        """
        Allows to have all method from the bot

        :return: List of all method
        """
        return 'register_bot', 'get_info_for_track_by_album', \
               'get_logger', 'deserialase_album', 'deserialase_music' \
               'deserialase_track'


if __name__ == '__main__':
    Deezer()
