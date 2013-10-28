from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import AdminBot
from AdminBot.views import hello, current_datetime
from AdminBot.login_user import login_user
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'AdminBot.views.home', name='home'),
    # url(r'^DjangoBot/', include('DjangoBot.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adminbot/', include('AdminBot.urls'))
)
