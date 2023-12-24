from django.core.management.base import BaseCommand
from django.apps import apps
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Initialize data for your app'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Initializing data...'))

        Poll = apps.get_model('poll', 'Poll')

        if Poll.objects.count() == 0:
            Poll.objects.create(
                id=1,
                is_active=True,
                access_code='1234',
                option_a='a',
                option_b='b',
                option_c='c',
                option_d='d',
                option_a_count=0,
                option_b_count=0,
                option_c_count=0,
                option_d_count=0
            )
        else:
            Poll.objects.exclude(id=1).delete()

        self.stdout.write(self.style.SUCCESS('Data initialization complete!'))
