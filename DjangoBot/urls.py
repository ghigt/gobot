from django.conf.urls import patterns, include, url
from AdminBot.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'AdminBot.views.home', name='home'),
    #url(r'^DjangoBot/', include('DjangoBot.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:

    (r'^$', main_page),

    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adminbot/', include('AdminBot.urls')),
)
