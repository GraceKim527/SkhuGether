from django.contrib import admin
from .models import Class, Professor, Classroom, Feedback
# Register your models here.

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'class_date1', 'class_date2', 'class_time1', 'class_time2']
    ordering = ['class_name']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['professor_name']
    ordering = ['professor_name']

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['classroom_unit', 'professor_name', 'class_name', 'class_date1', 'class_date2', 'class_time1', 'class_time2']
    ordering = ['classroom_unit', 'class_time1']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'feedback_date', 'user_phonenum', 'feedback_content']
    ordering = ['feedback_date']