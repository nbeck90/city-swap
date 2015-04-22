from django.apps import AppConfig


class MyAppConfig(AppConfig):
    """For signals to work on app ready"""
    name = 'profiles'

    def ready(self):
        print "should be working"
        import signals
