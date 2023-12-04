from django.conf import settings


def global_variables(_request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "APPS_IN_HEADER": settings.APPS_IN_HEADER,
    }
