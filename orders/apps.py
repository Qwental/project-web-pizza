from django.apps import AppConfig


class OrdersConfig(AppConfig):
    """
    To configure an application, create an apps.py module inside the application,
    then define a subclass of AppConfig there.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
