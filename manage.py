#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoBot.settings")

    from django.core.management import execute_from_command_line
    from django.core import management

    os.system('mysql --user=root --password=root -e"DROP DATABASE IF EXISTS testbot"')
    os.system('mysql --user=root --password=root -e"CREATE DATABASE testbot"')
    # Run the syncdb
    management.call_command('syncdb', interactive=False)

    # Create the super user and sets his password.
    from django.contrib.auth.models import User

    u = User(username='admin')
    u.set_password('password')
    u.is_superuser = True
    u.is_staff = True
    u.save()
    execute_from_command_line(sys.argv)
