# -*- coding: utf-8 -*-
__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import datetime
from AdminBot.Bot import settings
import logging
import logging.config
from AdminBot.models import Bot, LogError, LogInfo


class RegisterBot():
    """

    Allow to register a bot in database
    You just need to call the class RegisterBot in __init__()
    """
    def __init__(self, version, actif, log_bot,
                 error_bot, name, last_use, nb_iter=0):
        """

        :param version: Version of Bot
        :param actif: True or False
        :param log_bot: Path to the LogInfo
        :param error_bot: Path to the LogError
        :param name: Name of the bot
        :param nb_iter: 0 by default
        :param last_use: Date of today
        """
        logging.config.fileConfig(settings.CONFIG_LOG)
        self.logger = logging.getLogger("RegisterBot")
        self.__version = version
        self.__actif = actif
        self.__path_to_log_info = log_bot
        self.__path_to_log_error = error_bot
        self.__name = name
        self.__nb_iter = nb_iter
        self.__last_use = last_use
        self.__register_bot()

    def __register_bot(self):
        """

        Private method
        Allow to register a bot in database
        :return:
        """
        log = self.__register_log_info()
        log_error = self.__register_log_error()
        try:
            bot = Bot.objects.get(version=self.__version, name=self.__name)
            bot.save()
            self.logger.info("Mise à jour du Robot %s dans la BDD,"
                             " version %s",
                             self.__name, self.__version)
            return
        except Bot.DoesNotExist:
            bot = Bot(version=self.__version,
                      actif=self.__actif,
                      log_bot=log,
                      error_bot=log_error,
                      name=self.__name,
                      nb_iter=self.__nb_iter,
                      last_use=self.__last_use)
            bot.save()
            self.logger.info(
                "Enregistrement du Robot %s dans la BDD, version %s",
                self.__name, self.__version)

    def __register_log_error(self):
        """

        Private method
        Allow to register a LogError in database
        :return: LogError object
        """
        try:
            log = LogError.objects.get(path_to_log=self.__path_to_log_error)
            log.date = datetime.datetime.today()
            log.save()
            self.logger.info("Update de l'objet LogError pour %s",
                             self.__name)
            return log
        except LogError.DoesNotExist:
            log_error = LogError(date=datetime.datetime.today(),
                                 path_to_log=self.__path_to_log_error)
            log_error.save()
            self.logger.info("Sauvegarde de l'objet LogError pour %s",
                             self.__name)
            return log_error

    def __register_log_info(self):
        """

        Private method
        Allow to register a LogInfo in database
        :return: LogInfo object
        """
        try:
            log = LogInfo.objects.get(path_to_log=self.__path_to_log_info)
            log.date = datetime.datetime.today()
            log.save()
            self.logger.info("Update de l'objet LogInfo pour %s",
                             self.__name)
            return log
        except LogInfo.DoesNotExist:
            log_info = LogInfo(date=datetime.datetime.today(),
                               path_to_log=self.__path_to_log_info)
            log_info.save()
            self.logger.info("Sauvegarde de l'objet LogInfo pour %s",
                             self.__name)
            return log_info
