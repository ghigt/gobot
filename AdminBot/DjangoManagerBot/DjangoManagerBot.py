# -*- coding: utf-8 -*-

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

from AdminBot.Bot import settings
from AdminBot.Bot.Betaseries.Betaseries import Betaseries
import logging
import logging.config


class DjangoManagerBot():
    logging.config.fileConfig(settings.CONFIG_LOG)
    log = logging.getLogger("ManagerBot")
    RobotDict = dict()
    RobotDict["Betaserie"] = Betaseries

    def __init__(self):
        pass

    def register_bot_in_db(self, bot_base=None):
        if bot_base:
            bot = self.RobotDict[bot_base]()
            bot.register_bot()
            self.log.info("Le robot %s est enregistré dans Django", bot
            .__class__.__name__)
