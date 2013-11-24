# Create your views here.
from django.http import HttpResponse
import datetime

from django.http import *
from django.shortcuts import render_to_response, render
from django.template import RequestContext, Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from AdminBot.models import Bot
from AdminBot.DjangoManagerBot.DjangoManagerBot import DjangoManagerBot
from AdminBot.Bot.settings import REGISTER_BOTS as register_bot


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
    return render_to_response('registration/login.html',
                              {'username': username},
                              context_instance=RequestContext(request))


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def adminbot_main_page(request):
    if request.user.is_authenticated():
        t = loader.get_template('adminbot/index.html')
        context = Context({'robots': Bot.objects.all(),})
        print "coucou"
        return HttpResponse(t.render(context))
        #return render(request, 'adminbot/index.html', context)
    #return render_to_response('adminbot/index.html')

@login_required
def botRegister(request):
    registerbot = DjangoManagerBot()
    t = loader.get_template('adminbot/registerBot.html')
    context = Context({'list_robot': register_bot, 'robots': Bot.objects.all()})
    return HttpResponse(t.render(context))
