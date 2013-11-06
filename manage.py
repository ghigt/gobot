#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoBot.settings")

    from django.core.management import execute_from_command_line
    from django.core import management

    os.system('mysql --user=root --password=root -e"DROP DATABASE IF EXISTS testbot"')
    os.system('mysql --user=root --password=root -e"CREATE DATABASE testbot CHARACTER SET utf8"')
    os.system('rm data.db')
    # For server
    #os.system('mysql --user=root --password=bjtu2013sylimysql -e"DROP DATABASE IF EXISTS testbot"')
    #os.system('mysql --user=root --password=bjtu2013sylimysql -e"CREATE DATABASE testbot CHARACTER SET utf8"')
    # Run the syncdb
    management.call_command('syncdb', interactive=False)

    # Create the super user and sets his password.
    from django.contrib.auth.models import User

    u = User(username='admin')
    u.set_password('password')
    u.is_superuser = True
    u.is_staff = True
    u.save()

    d = User(username='Nkio')
    d.set_password('coucou')
    d.is_superuser = False
    d.is_staff = False
    d.save()
    execute_from_command_line(sys.argv)
