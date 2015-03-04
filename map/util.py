from map.models import *
from django.utils.datastructures import OrderedDict

def get_map(pos=(0,0), radius=5, method='max'):
	"""returns a map with center at `pos' and given `radius'"""
	x,y = pos
	mapdata = Field.objects.filter(x__gte=x-radius).filter(x__lte=x+radius).filter(y__gte=y-radius).filter(y__lte=y+radius)

	area = OrderedDict()
	# assume field with pk=1 is background
	space = FieldType.objects.get(pk=1)

	for u in xrange(y-radius, y+radius+1):
		if not area.has_key(u):
			area[u] = OrderedDict()
		for v in xrange(x-radius, x+radius+1):
			spacefield = Field()
			spacefield.fieldtype = space
			spacefield.x, spacefield.y = v,u
			area[u][v] = spacefield

	return area

