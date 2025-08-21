# backend/apps/api/apps.py  
from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.api'  # Changed from 'api' to 'apps.api'