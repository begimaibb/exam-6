from django.contrib import admin

# Register your models here.
from webapp.models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name', 'email']
    fields = ['name', 'email', 'text', 'created_date', 'updated_date', 'status']
    readonly_fields = ['created_date', 'updated_date']


admin.site.register(Guest, GuestAdmin)
