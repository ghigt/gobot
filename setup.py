from distutils.core import setup

setup(
    name='DjangoBot',
    version='0.1',
    packages=['AdminBot', 'AdminBot.Bot', 'AdminBot.Bot.bot', 'AdminBot.Bot.Http', 'AdminBot.Bot.Betaseries',
              'AdminBot.Bot.Betaseries.ObjectDeserialised', 'DjangoBot'],
    url='',
    license='',
    author='Nkio',
    author_email='',
    description='', requires=['requests', 'pytest_django', 'django']
)