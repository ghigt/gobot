__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import time
from datetime import date, datetime


class Timer:
    """
    Allow to make a timer for the different bots
    """
    def __init__(self):
        self.__date_begin = None
        self.__date_end = None
        self.__delta = None
        self.__days = None
        self.__hours = None
        self.__minutes = None

    def begin_bot(self):
        """
        Must be used when the robot start
        """
        self.__date_begin = datetime.now()

    def end_bot(self):
        """
        Must be used when the robot ends
        Set the news values inside the class and
        computing the different values
        """
        self.__date_end = datetime.now()
        self.__delta = self.__date_end - self.__date_begin
        self.__days = self.__delta.days
        self.__hours = self.__delta.seconds // 3600
        self.__minutes = (self.__delta.seconds // 60) % 60

    def get_minutes(self):
        """
        Allow to have the number of minutes
        The calculation is performed between begin_bot and end_bot
        :return: int
        """
        return self.__minutes

    def get_hours(self):
        """
        Allow to have the number of hours
        The calculation is performed between begin_bot and end_bot
        :return: int
        """
        return self.__days

    def get_seconds(self):
        """
        Allow to have the number of seconds
        The calculation is performed between begin_bot and end_bot
        :return: int
        """
        return self.__delta.seconds

    def get_day(self):
        """
        Allow to have the number of day
        The calculation is performed between begin_bot and end_bot
        :return: int
        """
        return self.__days

    def get_days_hours_minutes(self):
        """
        Allow to have a tuple with day hours minutes
        The calculation is performed between begin_bot and end_bot
        :return: tuple() with day, hours, minutes
        """
        return self.__days, self.__hours, self.__minutes

    def get_all_seconds(self):
        """
        Allow to have all seconds between begin_bot and end_bot
        :return: int
        """
        return self.__delta.total_seconds()