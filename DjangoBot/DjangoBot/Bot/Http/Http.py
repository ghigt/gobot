__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


class Http:
    typeHttp = 'http'
    request = list()

    def __init__(self):
        i = None

    def HttpType(self, typeHttp='http'):
        self.typeHttp = typeHttp

    def HttpType(self):
        return self.typeHttp

    def addRequest(self, request):
        newRequest = str()
        newRequest = request % self.typeHttp
        self.request.append(request)

