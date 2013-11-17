__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


class BotBase():
    def __init__(self):
        pass

    @staticmethod
    def get_api_key():
        raise NotImplementedError("Subclasses Should have implemented this")

    def search(self, value):
        raise NotImplementedError("Subclasses Should have implemented this")

    def get_info_for(self, value):
        raise NotImplementedError("Subclasses Should have implemented this")

    @staticmethod
    def get_logger(self):
        raise NotImplementedError("Subclasses Should have implemented this")

    def register_bot(self):
        raise NotImplementedError("Subclasses Should have implemented this")

    class Meta:
        abstract = True
