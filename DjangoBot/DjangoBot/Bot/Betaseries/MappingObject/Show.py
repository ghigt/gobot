__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Show(Base):
    __tablename__ = 'Show'
    id = Column(Integer, primary_key=True)
    idBetaSerie = Column(Integer)
    thetvdb_id = Column(Integer)
    imdb_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    seasons = Column(String)
    episodes = Column(String)
    followers = Column(String)
    comments = Column(String)
    similars = Column(String)
    characters = Column(String)
    creation = Column(String)
    genres = Column(String)
    length = Column(String)
    status = Column(String)
    language = Column(String)
    Episodes = relationship('Episode')
