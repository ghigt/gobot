__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import datetime
import logging
from AdminBot.models import Bot, LogError, LogInfo


class RegisterBot():
    """

    Allow to register a bot in database
    You just need to call the class RegisterBot in __init__()
    """
    logging.config.fileConfig("../configuration.cfg")
    log = logging.getLogger("RegisterBot")

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
            return log
        except LogError.DoesNotExist:
            log_error = LogError(date=datetime.datetime.today(),
                                 path_to_log=self.__path_to_log_error)
            log_error.save()
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
            return log
        except LogInfo.DoesNotExist:
            log_info = LogInfo(date=datetime.datetime.today(),
                               path_to_log=self.__path_to_log_info)
            log_info.save()
            return log_info