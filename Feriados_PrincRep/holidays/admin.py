from django.contrib import admin
from django .models import Holiday

@admin.register(Holiday)
class Holiday(admin.ModelAdmin):
    list_display = ('nome', 'data', 'tipo')
    search_fields = ('nome', 'tipo')
    list_filter = ('tipo',)
