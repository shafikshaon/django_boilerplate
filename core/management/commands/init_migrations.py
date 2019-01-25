import os

from django.core.management.base import BaseCommand

from django_boilerplate import settings


class Command(BaseCommand):
    help = 'Init Migrations'

    def handle(self, *args, **kwargs):
        custom_apps = settings.CUSTOM_APPS

        for app in custom_apps:
            _current_app = os.path.join(app.replace('.', os.sep), 'migrations')
            if not os.path.isdir(_current_app) and not os.path.exists(_current_app):
                self.stdout.write('Creating migration folder for... [' + self.style.SUCCESS(_current_app) + ']')
                os.makedirs(_current_app)
                init_file = open(os.path.join(_current_app, '__init__.py'), 'w')
                init_file.close()
            else:
                self.stdout.write('Migrations folder already exists for... [' + self.style.ERROR(_current_app) + ']')

        self.stdout.write(self.style.SUCCESS('Command executed successfully.'))
