__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

"""All information for all robots
    We need to import all settings from all robots"""
import os
from AdminBot.Bot.Betaseries import settings as settings_betaserie
from AdminBot.Bot.Deezer import settings as settings_deezer

#Generals Information

PROJECT_NAME_FOR_HTTP_HEADER = "SyliBot"

#Informations for Betaserie's Bot
API_KEY_BETASERIE = settings_betaserie.API_KEY_BETASERIE
API_VERSION_BETASERIE = settings_betaserie.API_VERSION_BETASERIE
HTTP_MODE = settings_betaserie.HTTP_MODE
CONFIG_LOG = os.path.join(os.path.dirname(__file__), "configuration.cfg")
REGISTER_BOTS = ('Betaserie', 'Deezer')

#Informations for Deezer's Bot
#API_KEY_DEEZER = settings_deezer.API_KEY_DEEZER
#API_VERSION_DEEZER = settings_deezer.API_VERSION_DEEZER
