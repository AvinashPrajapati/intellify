"""SchoolManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', homeView, name='homepage'),
    path('admin/', admin.site.urls),
    path('login/', loginView, name = 'login'),
    path('logout/', logoutView, name = 'logout'),
    path('student/', include(('student.urls', 'student'), namespace='student')),
    path('faculty/', include(('faculty.urls', 'faculty'), namespace='faculty')),
]

# static and media file location mentioned
#we ca use this also
#if settings.DEBUG: then these two urls but in production we have to remove this
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
