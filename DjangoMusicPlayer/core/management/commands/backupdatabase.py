from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.utils import timezone
from datetime import datetime


class Command(BaseCommand):
    help = "Get a Backup of your Database"

    def add_arguments(self, parser):
        parser.add_argument("-p", "--path", type=str, default='backups/', help="Path of the saved backup")

    def handle(self, *args, **options):
        dt_str = datetime.strftime(timezone.now(), "%Y-%m-%d_%H-%M-%S")
        path = options['path'] if options['path'].endswith('/') else options['path'] + '/'
        file_name = f'DB-{dt_str}.json'
        try:
            with open(f"{path}{file_name}", "w+") as f:
                call_command('dumpdata', stdout=f)
                self.stdout.write(self.style.SUCCESS('Database Backed up successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('No such directory: Invalid Directory Path'))

