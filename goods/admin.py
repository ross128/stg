from django.contrib import admin
from goods.models import *

class GoodAssignmentInlineAdmin(admin.TabularInline):
	model = GoodAssignment
	fields = ('good', 'count')
	extra = 1

class StockAdmin(admin.ModelAdmin):
	inlines = (GoodAssignmentInlineAdmin,)

admin.site.register(Good)
admin.site.register(Stock, StockAdmin)
admin.site.register(GoodAssignment)
