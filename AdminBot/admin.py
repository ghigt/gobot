__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


from django.contrib import admin
from AdminBot.models import Show, Episode, Genre

admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(Genre)