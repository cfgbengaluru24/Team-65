from django import template
from datetime import datetime, timedelta, time

register = template.Library()

@register.filter(name='add')
def add(value, arg):
    # Parse the input value as a time object
    if isinstance(value, time):
        # Combine with today's date to make it a datetime object
        now = datetime.now()
        combined_datetime = datetime.combine(now.date(), value)
        # Add the minutes
        new_datetime = combined_datetime + timedelta(minutes=int(arg))
        # Return only the time part
        return new_datetime.time()
    else:
        raise ValueError("The value provided is not a time object")


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

