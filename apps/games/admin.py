
from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from .models import Game, Category
from django.db import models

# Modelo proxy para el panel de control
class ControlProxy(Game):
	class Meta:
		proxy = True
		verbose_name = 'Control'
		verbose_name_plural = 'Control'



class ControlAdmin(admin.ModelAdmin):
	change_list_template = "admin/control_changelist.html"
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
	def has_change_permission(self, request, obj=None):
		return False

	def changelist_view(self, request, extra_context=None):
		extra_context = extra_context or {}
		extra_context['control_url'] = '/panel/control/'
		return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(ControlProxy, ControlAdmin)