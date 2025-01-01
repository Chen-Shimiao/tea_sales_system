# admin.py
from django.contrib import admin
from .models import Category, Origin, Promotion


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'description')
    search_fields = ('name',)
    list_filter = ('parent',)

admin.site.register(Category, CategoryAdmin)

class OriginAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'description')
    search_fields = ('name', 'country')
    list_filter = ('country',)

admin.site.register(Origin, OriginAdmin)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'promotion_type', 'start_time', 'end_time', 'is_active']
    list_filter = ['promotion_type', 'is_active']
    search_fields = ['name']