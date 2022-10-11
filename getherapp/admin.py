from django.contrib import admin
from .models import Subject, Professor, Classroom, Class, Feedback

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'kind', 'code', 'name']
    ordering = ['name']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['name']

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['id','kwan_num', 'kwan_name', 'unit']
    ordering = ['kwan_num', 'kwan_name', 'unit']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'div', 'date1', 'date2', 'time1', 'time2', 'room_id']
    ordering = ['date1', 'date2', 'time1', 'time2', 'room_id']

admin.site.register(Feedback)