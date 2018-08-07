from django.apps import AppConfig
from django.conf import settings

from simpl import subscribe


class {{cookiecutter.app_slug|title}}Config(AppConfig):
    name = '{{cookiecutter.app_slug}}'

    def ready(self):
        subscribe('user')
        subscribe(settings.GAME_SLUG)
