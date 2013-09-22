__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Episode(Base):
    __tablename__ = 'Episode'
    id = Column(Integer, primary_key=True)
    idBetaSerie = Column(Integer)
    title = Column(String)
    season = Column(Integer)
    episode = Column(Integer)
    show_id = Column(Integer)
    show_title = Column(String)
    code = Column(Integer)
    description = Column(String)
    date = Column(Date)
    show_id = Column(Integer, ForeignKey('show.id'))
