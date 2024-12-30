from django.contrib import admin
from django.apps import apps

def auto_register_all_models():
    # Get all installed apps' models
    for model in apps.get_models():
        try:
            # Try registering the model with a default ModelAdmin
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            # Skip models that are already registered
            pass
auto_register_all_models()        
