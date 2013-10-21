from django.db import models

# Create your models here.

# Debut Model Bot


class Show(models.Model):
    thetvdb_id = models.IntegerField(null=True)
    imdb_id = models.IntegerField(null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    seasons = models.PositiveIntegerField()
    nbepisode = models.PositiveIntegerField()
    follower = models.PositiveIntegerField()
    comment = models.CharField(max_length=500)
    similars = models.CharField(max_length=200)
    characters = models.CharField(max_length=500)
    creation = models.CharField(max_length=4)
    genre = models.CharField(max_length=50)
    lenght = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    idbetaserie = models.IntegerField(null=True)

    def __unicode__(self):
        return self.title


class Episode(models.Model):
    title = models.CharField(max_length=200)
    season = models.PositiveSmallIntegerField()
    episode = models.PositiveIntegerField()
    showid = models.PositiveIntegerField()
    show_title = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateField()
    show = models.ForeignKey(Show)

    def __unicode__(self):
        return u'%s - %s' % (self.show_title, self.title)


class Genre(models.Model):
    type_genre = models.CharField(max_length=26)

    def __unicode__(self):
        return self.type_genre


class GenreToShow(models.Model):
    id_genre = models.ForeignKey(Genre)
    id_show = models.ForeignKey(Show)

# Fin Model Bot