__author__ = 'Alexandre Cloquet'


class Episode(object):
    def __init__(self, idBetaSerie, title, season, episode, show_id,
                 show_title, code, description,
                 date):
        self.idBetaSerie = idBetaSerie
        self.title = title
        self.season = season
        self.episode = episode
        self.show_id = show_id
        self.show_title = show_title
        self.code = code
        self.description = description
        self.date = date
