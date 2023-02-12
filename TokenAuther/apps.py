from django.apps import AppConfig


class TokenautherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TokenAuther'

    def ready(self):
        import TokenAuther.signals