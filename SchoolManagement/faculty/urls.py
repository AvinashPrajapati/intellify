from django.urls import path
from .views import * 

# url paths for teacher actions
urlpatterns = [
    path('', teacherProfile, name='teacherprofile'),
    path('teacher-register/', teacherRegister, name='teacherregister'),
]
