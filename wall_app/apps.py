from django.apps import AppConfig


class WallAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wall_app'

    def ready(self):
        import wall_app.signals
