from django.contrib import admin
from colony.models import *

class FieldAssignmentInlineAdmin(admin.TabularInline):
	model = FieldAssignment
	fields = ('field', 'x', 'y')
	extra = 1

class BuildingPropertyAssignmentInlineAdmin(admin.TabularInline):
	model = BuildingPropertyAssignment
	extra = 1

class BuildingAdmin(admin.ModelAdmin):
	model = Building
	inlines = (BuildingPropertyAssignmentInlineAdmin,)

class ColonyAdmin(admin.ModelAdmin):
	inlines = (FieldAssignmentInlineAdmin,)
	list_display = ('name', 'owner')
	list_filter = ('owner',)
	list_per_page = 100
	search_fields = ('name',)
	fieldsets = [
		('Colony', {
			'fields': ['name', 'owner', 'stock', 'energy'],
		}),
	]

admin.site.register(Colony, ColonyAdmin)
admin.site.register(Field)
admin.site.register(FieldAssignment)
admin.site.register(Building, BuildingAdmin)
admin.site.register(BuildingAssignment)
admin.site.register(BuildingConstruction)
admin.site.register(BuildingProperty)
admin.site.register(BuildingPropertyAssignment)
