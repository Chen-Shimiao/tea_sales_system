from django.contrib import admin

from sales_system.models import Announcement


# Register your models here.
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'content')
    list_editable = ('is_active',)
    ordering = ('-created_at',)