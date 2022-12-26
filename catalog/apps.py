from django.apps import AppConfig

# We have only one app, which is catalog. Our apps should be described here.
class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
