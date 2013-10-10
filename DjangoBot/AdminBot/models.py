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
    title = models.CharField(max_length=255)
    description = models.TextField()
    seasons = models.CharField(max_length=255)
    episodes = models.CharField(max_length=255)
    followers = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    similars = models.CharField(max_length=255)
    characters = models.CharField(max_length=255)
    creation = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    #Episodes = relationship('Episode')


class Episode(models.Model):
    __tablename__ = 'Episode'
    id = models.IntegerField(primary_key=True)
    idBetaSerie = models.IntegerField()
    title = models.CharField(max_length=255)
    season = models.IntegerField()
    episode = models.IntegerField()
    show_id = models.IntegerField()
    show_title = models.CharField(max_length=255)
    code = models.IntegerField()
    description = models.TextField()
    date = models.DateField()
    show_id = models.ForeignKey('Show')
#Fin Betaseries