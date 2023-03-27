from django.apps import AppConfig


class GroupControlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'group_control'

    def ready(self):
        import group_control.signals
