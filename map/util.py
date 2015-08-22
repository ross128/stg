from map.models import *
from django.utils.datastructures import OrderedDict
import hashlib
import numpy as np

def generate_map_slice(indices, map_seed=0, slice_size=10):
	"""generates a map slice of given size randomly"""
	this_seed = int(hashlib.sha256(str(tuple([map_seed, indices])).encode('utf-8')).hexdigest(), base=16) % (2**32)
	np.random.seed(this_seed)
	data = np.random.uniform(size=(slice_size, slice_size))

	# probabilities (here: for three map FieldTypes)
	probabilities = [0.99, 0.997]
	data = np.digitize(np.reshape(data, slice_size*slice_size), probabilities).reshape((slice_size, slice_size))

	return data

def get_map(pos=(0,0), radius=5, method='max'):
	"""returns a map with center at `pos' and given `radius'"""
	x,y = pos
	map_seed = 98743502345983476198437592375
	slice_size = 10
	area = OrderedDict()
	slices = {}

	all_fieldtypes = {}
	for ft in FieldType.objects.all():
		all_fieldtypes[ft.pk] = ft
	for cur_y in range(y-radius, y+radius+1):
		for cur_x in range(x-radius, x+radius+1):
			cur_pos = np.array([cur_x,cur_y])
			cur_i = cur_pos // slice_size
			cur_mod_x, cur_mod_y = cur_pos % slice_size

			if not tuple(cur_i) in slices:
				slices[tuple(cur_i)] = generate_map_slice(cur_i, map_seed=map_seed, slice_size=slice_size)
			if not cur_y in area:
				area[cur_y] = OrderedDict()

			# add randomly generated field
			field = Field()
			field.fieldtype = all_fieldtypes[int(slices[tuple(cur_i)][cur_mod_x][cur_mod_y]) + 1]
			field.x, field.y = cur_x, cur_y
			area[cur_y][cur_x] = field

	# add fields from database to map
	mapdata = Field.objects.filter(x__gte=x-radius).filter(x__lte=x+radius).filter(y__gte=y-radius).filter(y__lte=y+radius)
	for field in mapdata:
		area[field.y][field.x] = field

	return area

