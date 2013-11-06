# Create your views here.
from django.http import HttpResponse
import datetime

from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def main_page(request):
    return render_to_response('index.html')


def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('adminbot/index.html')
    return render_to_response('registration/login.html', {'username': username}, context_instance=RequestContext(request))


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def adminbot_main_page(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render_to_response('adminbot/index.html')


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)