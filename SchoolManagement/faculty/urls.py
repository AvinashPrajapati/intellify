from django.urls import path
from .views import * 

urlpatterns = [
    path('', teacherProfile, name='teacherprofile'),
    path('teacher-register/', teacherRegister, name='teacherregister'),
]