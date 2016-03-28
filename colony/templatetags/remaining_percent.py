from django.template.defaulttags import register

@register.filter(name='remaining_percent')
def remaining_percent(percentage):
	try:
		return 100.0 - percentage
	except TypeError:
		return 0
