from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies value by arg and returns the result."""
    try:
        return value * arg
    except (TypeError, ValueError):
        return value  # Fallback if the multiplication fails
