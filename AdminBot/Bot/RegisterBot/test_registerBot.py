from unittest import TestCase

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoBot.settings'
from AdminBot.models import Bot, LogInfo, LogError
from AdminBot.Bot.RegisterBot.RegisterBot import RegisterBot
from datetime import datetime
from django.core.management import call_command
call_command('syncdb', interactive=True)


class TestRegisterBot(TestCase):
    def setUp(self):
        bot = RegisterBot(version=0.01, actif=True,
                          log_bot="BetaserieLogInfo.log",
                          error_bot="BetaserieLogError.log", name="Betaserie",
                          last_use=datetime.today())
        self.bot_1 = Bot.objects.get()
        self.log_info = LogInfo.objects.get()
        self.log_error = LogError.objects.get()

    def test____register_bot(self):
        assert self.bot_1.version == u"0.01"
        assert self.bot_1.actif is True
        assert self.bot_1.name == "Betaserie"
        assert self.bot_1.name != "Betaserie"
        assert self.bot_1.nb_iter == 0
        assert self.bot_1.nb_iter != 1

    def test____register_log_error(self):
        assert self.log_error.error is True
        assert self.log_error.error is not False
        assert self.log_error.path_to_log == "BetaserieLogError.log"
        assert self.log_error.path_to_log != "BetaserieLogErrorRest.log"

    def test____register_log_info(self):
        assert self.log_info.error is False
        assert self.log_info.error is not True
        assert self.log_info.path_to_log == "BetaserieLogInfo.log"
        assert self.log_info.path_to_log != "BetaserieLogInfoTest.log"
