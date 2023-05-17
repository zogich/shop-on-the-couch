from django import template
from backend import settings
from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def hmr_script(path):
    origin = ''
    if settings.DEBUG and settings.VITE_DEV_SERVER:
        origin = f'http://{settings.VITE_DEV_SERVER}'
    else:
        path = static(path)
    return format_html(
        mark_safe('<script type="module" src="{}{}"></script>'),
        origin,
        path
    )


@register.simple_tag
def is_debug():
    return settings.DEBUG
