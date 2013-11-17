__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"

from django.conf.urls import patterns, url

urlpatterns = patterns('AdminBot.views',
                       url(r'^$', 'adminbot_main_page'),
                       )
