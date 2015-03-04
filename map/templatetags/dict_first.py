from __future__ import unicode_literals
from django import template

register = template.Library()

@register.filter(is_safe=True)
def iter_first(value):
	"""Returns the first item of an iterable."""
	if isinstance(value, dict):
		value = value.values()
	try:
		return next(iter(value))
	except StopIteration:
		return ''

