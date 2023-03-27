from django.apps import AppConfig


class AccountControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account_control'

    def ready(self):
        import account_control.signals
