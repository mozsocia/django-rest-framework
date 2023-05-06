from django.core.management.base import BaseCommand
from first_app.seed import seed_data


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        seed_data()
        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
