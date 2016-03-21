from django.contrib import admin
from ships.models import *

class ShipModuleAssignmentInlineAdmin(admin.TabularInline):
	model = ModuleAssignment
	fields = ('module', 'count')
	extra = 1

class ShipAdmin(admin.ModelAdmin):
	inlines = (ShipModuleAssignmentInlineAdmin,)
	list_display = ('name', 'shipclass', 'owner', 'x', 'y')
	list_filter = ('shipclass', 'owner')
	list_per_page = 100
	search_fields = ('name',)
	fieldsets = [
		('Ship', {
			'fields': ['name', 'shipclass', 'owner', 'x', 'y'],
		}),
	]
admin.site.register(ShipClass)
admin.site.register(Ship, ShipAdmin)
admin.site.register(Module)
admin.site.register(ModuleAssignment)
admin.site.register(ShipProperty)
admin.site.register(ModulePropertyAssignment)

