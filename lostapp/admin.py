from django.contrib import admin
from .models import Lost, Comment

# Register your models here.
@admin.register(Lost)
class LostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'classroom', 'created_at']
    ordering = ['classroom','created_at','updated_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'lost_id', 'content', 'created_at']
    ordering = ['lost_id','content']