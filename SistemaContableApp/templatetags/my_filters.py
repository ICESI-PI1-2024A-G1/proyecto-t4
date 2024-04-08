from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Custom template filter to add a CSS class to a form field.

    Args:
        value (django.forms.BoundField): The bound form field.
        arg (str): The CSS class to be added.

    Returns:
        django.forms.BoundField: The bound form field with the added CSS class.
    """
    
    return value.as_widget(attrs={'class': arg})
