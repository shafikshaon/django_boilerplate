import os
import shutil

from django.core.management.base import BaseCommand

from django_boilerplate import settings


class Command(BaseCommand):
    help = 'Init Migrations'

    def handle(self, *args, **kwargs):
        custom_apps = settings.CUSTOM_APPS

        for app in custom_apps:
            _current_app = os.path.join(app.replace('.', os.sep), 'migrations')

            if not os.path.isdir(_current_app) and not os.path.exists(_current_app):
                self.stdout.write('No migrations available for... [' + self.style.SUCCESS(_current_app) + ']')
                self.stdout.write('You can run [' + self.style.NOTICE('python manage.py '
                                                                      'init_migrations') + ']')
            else:
                shutil.rmtree(_current_app)
                os.makedirs(_current_app)
                init_file = open(os.path.join(_current_app, '__init__.py'), 'w')
                init_file.close()
                self.stdout.write('Remove migrations for... [' + self.style.ERROR(_current_app) + ']')

        self.stdout.write(self.style.SUCCESS('Command executed successfully.'))
