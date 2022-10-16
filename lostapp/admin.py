from django.contrib import admin
from .models import Lost

# Register your models here.
@admin.register(Lost)
class LostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'classroom', 'created_at']
    ordering = ['classroom','created_at','updated_at']