from django.db import models

# Create your models here.


class Log(models.Model):
    error = models.PositiveSmallIntegerField()
    date = models.DateField()
    path_to_log = models.CharField(max_length=500)


class Bot(models.Model):
    version = models.CharField(max_length=10)
    actif = models.PositiveSmallIntegerField()
    log_bot = models.ForeignKey(Log)
    error_bot = models.ForeignKey(Log, related_name="error_bot")
    name = models.CharField(max_length=100, db_index=True)
    nb_iter = models.PositiveIntegerField()
    last_use = models.DateTimeField()
    launch_time = models.DateTimeField()
    elapsed_time = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.version)

# Debut Model Bot


class Show(models.Model):
    thetvdb_id = models.IntegerField(null=True)
    imdb_id = models.IntegerField(null=True)
    title = models.CharField(db_index=True, max_length=200)
    description = models.TextField()
    seasons = models.PositiveIntegerField()
    nbepisode = models.PositiveIntegerField()
    creation = models.CharField(max_length=4)
    genre = models.CharField(max_length=50)
    lenght = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    idbetaserie = models.IntegerField(db_index=True, null=True)

    def __unicode__(self):
        return self.title


class Episode(models.Model):
    title = models.CharField(db_index=True, max_length=200)
    season = models.PositiveSmallIntegerField()
    episode = models.PositiveIntegerField()
    showid = models.PositiveIntegerField()
    show_title = models.CharField(db_index=True, max_length=200)
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

# Debut du model Movie


class Movie(models.Model):
    title = models.CharField(db_index=True, max_length=500)
    id_tvdb = models.PositiveIntegerField()
    description = models.TextField()
    dateOnAir = models.DateField()
    genre = models.ForeignKey("GenreToMovie")


class GenreToMovie(models.Model):
    id_genre = models.ForeignKey(Genre)
    id_movie = models.ForeignKey(Movie)
