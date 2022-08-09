from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'id',)
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id',)