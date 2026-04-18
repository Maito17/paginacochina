
from django.contrib import admin
from .models import Game, Category, SocialNetwork, SubscriptionPlan


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'android_type', 'created_at')
	list_filter = ('category', 'android_type', 'created_at')
	search_fields = ('title', 'description')
	fieldsets = (
		('Informacion basica', {
			'fields': ('title', 'description', 'category', 'tags'),
		}),
		('Imagenes', {
			'fields': ('thumbnail', 'image1', 'image2'),
		}),
		('Descargas y clasificacion', {
			'fields': ('download_url', 'download_url_android', 'android_type'),
		}),
		('Metricas', {
			'fields': ('views_count',),
		}),
	)

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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')
	search_fields = ('name',)

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', 'is_active')
	list_editable = ('is_active',)
	search_fields = ('name',)

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'is_active')
	list_editable = ('is_active',)
	search_fields = ('title',)

admin.site.register(ControlProxy, ControlAdmin)