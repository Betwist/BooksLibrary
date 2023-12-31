from django.apps import AppConfig


class ClientApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientapi'

    def ready(self):
        import clientapi.signals
