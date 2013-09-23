# Create your models here.

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

from django.db import models

#Debut Betaseries
#TODO Verifier qu'il ne manque pas de base pour Betaserie
class Show(models.Model):
    __tablename__ = 'Show'
    id = models.IntegerField(primary_key=True)
    idBetaSerie = models.IntegerField()
    thetvdb_id = models.IntegerField()
    imdb_id = models.IntegerField()
    title = models.CharField()
    description = models.CharField()
    seasons = models.CharField()
    episodes = models.CharField()
    followers = models.CharField()
    comments = models.CharField()
    similars = models.CharField()
    characters = models.CharField()
    creation = models.CharField()
    genres = models.CharField()
    length = models.CharField()
    status = models.CharField()
    language = models.CharField()
    #Episodes = relationship('Episode')


class Episode(models.Model):
    __tablename__ = 'Episode'
    id = models.IntegerField(primary_key=True)
    idBetaSerie = models.IntegerField()
    title = models.CharField()
    season = models.IntegerField()
    episode = models.IntegerField()
    show_id = models.IntegerField()
    show_title = models.CharField()
    code = models.IntegerField()
    description = models.CharField()
    date = models.DateField()
    show_id = models.ForeignKey('Show')
#Fin Betaseries