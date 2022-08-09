from django.urls import path
from .views import studentProfile, studentRegister

urlpatterns = [
    path('', studentProfile, name='studentprofile'),
    path('student-register/', studentRegister, name='studentregister'),
]