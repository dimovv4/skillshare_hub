from django import template

register = template.Library()

@register.filter
def price_format(value):
    try:
        return f"{float(value):.2f} €"
    except:
        return value

@register.filter
def is_instructor(user):
    return getattr(user, "is_instructor", False)
