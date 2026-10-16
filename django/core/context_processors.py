from django.conf import settings


def app_settings(request):
    """Expose the bits of configuration templates actually need."""
    return {
        "app_name": settings.APP_NAME,
        "oauth_enabled": settings.OAUTH_ENABLED,
    }
