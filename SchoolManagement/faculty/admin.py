from django.contrib import admin
from .models import *

# Registering faculty app models here.
# list_display is used to display table field name in admin panel
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','id','member_type', 'first_name', 'last_name', 'email', 'is_superuser')
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id',)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'id',)
    
@admin.register(Class) 
class ClassAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'id', 'time')
