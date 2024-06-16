import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reminder.settings')
import django
from django.conf import settings

if not settings.configured:
    django.setup()

from user_management.models import BasicUser

def do_some_stuff():
    print(len(BasicUser.objects.all()))


if __name__ == "__main__":
    do_some_stuff()