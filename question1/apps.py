from django.apps import AppConfig

class Question1Config(AppConfig):
    name = 'question1'

    def ready(self):
        import question1.signals  # This will connect the signals when the app is ready
