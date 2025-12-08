from django.apps import apps
from django.contrib.sites.models import Site

from pinax_theme_bootstrap.conf import settings as theme_settings


def theme(request):
    ctx = {
        "THEME_ADMIN_URL": theme_settings.THEME_ADMIN_URL,
        "THEME_CONTACT_EMAIL": theme_settings.THEME_CONTACT_EMAIL,
    }

    if apps.is_installed("django.contrib.sites"):
        try:
            site = Site.objects.get_current(request)
        except Exception:
            # avoid breaking rendering if sites is misconfigured
            pass
        else:
            ctx.update({
                "SITE_NAME": site.name,
                "SITE_DOMAIN": site.domain,
            })

    return ctx
