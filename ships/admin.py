from django.contrib import admin
from ships.models import *

admin.site.register(ShipClass)
admin.site.register(Ship)
admin.site.register(Module)
admin.site.register(ModuleAssignment)

