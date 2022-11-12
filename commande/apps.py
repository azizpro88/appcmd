from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class CommandeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commande'
    
class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'