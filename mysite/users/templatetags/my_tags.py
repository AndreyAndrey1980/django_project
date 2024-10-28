from django import template

register = template.Library()


# Шаблонный фильтр
@register.filter
def my_slice(value, count=100):
    return value[:count]


@register.filter
def my_media(data):
    if data:
        return f'/catalog/media/{data}'
    return '#'
