from django.db import models

# Create your models here.


class Log(models.Model):
    date = models.DateField()
    path_to_log = models.CharField(max_length=500)

    class Meta:
        abstract = True


class LogError(Log):
    error = models.BooleanField(default=True)


class LogInfo(Log):
    error = models.BooleanField(default=False)


class Bot(models.Model):
    version = models.CharField(max_length=10)
    actif = models.BooleanField(default=True)
    log_bot = models.ForeignKey(LogInfo)
    error_bot = models.ForeignKey(LogError)
    name = models.CharField(max_length=100, db_index=True)
    nb_iter = models.PositiveIntegerField()
    last_use = models.DateTimeField()
    launch_time = models.DateTimeField(null=True, blank=True)
    elapsed_time = models.CharField(null=True, blank=True, max_length=200)

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

# Fin du model Movie

# Debut du model Music

class Album(models.Model):
    id_album = models.IntegerField(db_index = True)
    title = models.CharField(max_length=45)
    link = models.CharField(max_length=100)
    cover = models.CharField(max_length=100)
    nb_tracks = models.IntegerField()
    duration = models.IntegerField()
    fans = models.IntegerField()
    rating = models.IntegerField()
    release_date = models.DateField()
    available = models.BooleanField(default=False)
    artist = models.CharField(max_length=45)

    def __unicode__(self):
        return self.title


class Music(models.Model):
    id_music = models.IntegerField(db_index = True)
    title = models.CharField(max_length=45)
    link = models.CharField(max_length=100)
    duration = models.IntegerField()
    rank = models.IntegerField()
    preview_link = models.CharField(max_length=100)
    artist = models.CharField(max_length=45)

    def __unicode__(self):
        return self.title


class Track(models.Model):
    id_track = models.IntegerField(db_index = True)
    album = models.ForeignKey(Album)
    music = models.ForeignKey(Music)
    position = models.IntegerField()

# Fin du model Music

# Debut du model Manga/Anime

class Anime(models.Model):
    id_anime = models.IntegerField(db_index = True)
    english_title = models.CharField(max_length=45)
    japanese_title = models.CharField(max_length=45)
    image_url = models.CharField(max_length=100)
    type_anime = models.CharField(max_length=45)
    number_episodes = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=45)
    id_myanimelist = models.IntegerField()

class Manga(models.Model):
    id_manga = models.IntegerField(db_index = True)
    english_title = models.CharField(max_length=45)
    japanese_title = models.CharField(max_length=45)
    image_url = models.CharField(max_length=100)
    type_anime = models.CharField(max_length=45)
    number_chapters = models.IntegerField()
    number_volumes = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=45)
    id_myanimelist = models.IntegerField()

