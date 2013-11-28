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
import time


def main_page(request):
    return render_to_response('index.html', RequestContext(request))


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
        robots = Bot.objects.all()
        context = Context({'robots': robots, })
        return HttpResponse(t.render(context))


@login_required
def bot_register(request):
    t = loader.get_template('adminbot/registerBot.html')
    robots = Bot.objects.all()
    tmp = list()
    for bot_static in register_bot:
        for bot in robots:
            if bot_static in bot.name:
                pass
            else:
                tmp.append(bot_static)
    context = RequestContext(request, {'list_robot': tmp})
    return HttpResponse(t.render(context))


@login_required
def save_bot(request):
    register_bot = DjangoManagerBot()
    bot = request.POST['bot']
    register_bot.register_bot_in_db(bot)
    time.sleep(3)
    return render_to_response(bot + '.html', context_instance=RequestContext(
        request))
