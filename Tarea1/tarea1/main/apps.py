from django.apps import AppConfig

#no se modifican
class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
    def ready(self):
        import main.signals
