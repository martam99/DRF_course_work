import os

from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('email'),
            first_name=os.getenv('first_name'),
            last_name=os.getenv('last_name'),
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        user.set_password(os.getenv('password'))
        user.save()
