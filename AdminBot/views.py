# Create your views here.
from django.http import HttpResponse
import datetime


def home(request):
    text = """<h1>Bienve sur mon blog !</h1>
            <p>Les crepes bretonnes ca tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)