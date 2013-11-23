__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return HttpResponseRedirect('/admin/')
    return render_to_response('registration/login.html',
                              context_instance=RequestContext(request))
