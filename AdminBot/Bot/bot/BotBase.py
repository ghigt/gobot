__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

import abc


class BotBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def get_api_key(self):
        raise NotImplementedError("Subclasses Should have implemented this")

    @abc.abstractmethod
    def search(self, value):
        raise NotImplementedError("Subclasses Should have implemented this")

    @abc.abstractmethod
    def get_info_for(self, value):
        raise NotImplementedError("Subclasses Should have implemented this")

    @abc.abstractmethod
    def get_logger(self):
        raise NotImplementedError("Subclasses Should have implemented this")

    @abc.abstractmethod
    def register_bot(self):
        raise NotImplementedError("Subclasses Should have implemented this")

    @abc.abstractmethod
    def get_method(self):
        raise NotImplementedError("Subclasses Should have implemented this")