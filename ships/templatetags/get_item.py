from django.template.defaulttags import register

@register.filter(name='get_y')
def get_y(dictionary, key):
	return dictionary.get(key, {})

@register.filter(name='get_x')
def get_x(dictionary, key):
	return dictionary.get(key)

