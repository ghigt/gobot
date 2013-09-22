__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


class Show(object):
    def __init__(self, idBetaSerie, thetvdb_id, imdb_id, title,
                 description, seasons, episodes, followers,
                 comments, similars, characters, creation, genres, length, status, language):
        self.idBetaSerie = idBetaSerie
        self.thetvdb_id = thetvdb_id
        self.imdb_id = imdb_id
        self.title = title
        self.description = description
        self.seasons = seasons
        self.episodes = episodes
        self.followers = followers
        self.comments = comments
        self.similars = similars
        self.characters = characters
        self.creation = creation
        self.genres = genres
        self.length = length
        self.status = status
        self.language = language
