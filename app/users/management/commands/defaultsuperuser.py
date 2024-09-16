from django.core.management.base import BaseCommand
from django.utils import timezone
from app.users.models import Account

class Command(BaseCommand):
    help = 'Create Superuser'

    def handle(self, *args, **options):
        print("Creating Superuser...")
        acc, created = Account.objects.get_or_create(
            name="Superuser",
            email="superuser@duel.com",
            is_superuser=True,
            is_admin=True
        )
        if created:
            acc.set_password('pass')
            acc.save()
        print("Superuser End!")