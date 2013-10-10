__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


class Bot(object):
    def search(self, value):
        raise NotImplementedError

    def get_info_for(self, value):
        raise NotImplementedError

    def get_logger(self):
        raise NotImplementedError