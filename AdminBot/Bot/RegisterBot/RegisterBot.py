__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import datetime
from AdminBot.models import Bot, LogError, LogInfo


class RegisterBot():
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
        self.version = version
        self.actif = actif
        self.path_to_log_info = log_bot
        self.path_to_log_error = error_bot
        self.name = name
        self.nb_iter = nb_iter
        self.last_use = last_use
        self.register_bot()

    def register_bot(self):
        log = self.register_log_info()
        log_error = self.register_log_error()
        try:
            bot = Bot.objects.get(version=self.version, name=self.name)
            return bot
        except Bot.DoesNotExist:
            bot = Bot(version=self.version,
                      actif=self.actif,
                      log_bot=log,
                      error_bot=log_error,
                      name=self.name,
                      nb_iter=self.nb_iter,
                      last_use=self.last_use)
            bot.save()

    def register_log_error(self):
        try:
            log = LogError.objects.get(error=True,
                                       path_to_log=self.path_to_log_error)
            log.date = datetime.datetime.today()
            log.save()
            return log
        except LogError.DoesNotExist:
            log_error = LogError(error=True,
                                 date=datetime.datetime.today(),
                                 path_to_log=self.path_to_log_error)
            log_error.save()
            return log_error

    def register_log_info(self):
        try:
            log = LogInfo.objects.get(error=False,
                                      path_to_log=self.path_to_log_error)
            log.date = datetime.datetime.today()
            log.save()
            return log
        except LogInfo.DoesNotExist:
            log_info = LogInfo(error=False,
                               date=datetime.datetime.today(),
                               path_to_log=self.path_to_log_info)
            log_info.save()
            return log_info