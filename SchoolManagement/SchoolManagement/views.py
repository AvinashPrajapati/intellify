from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from faculty.models import *
from student.models import Student
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def homeView(request):
    template_name = 'homepage.html'
    if request.user.is_authenticated:
        if request.user.member_type == 'teacher':
            return redirect('faculty:teacherprofile')
        else:
            return redirect('student:studentprofile')

    return render(request, template_name=template_name)


def loginView(request):
    if request.user.is_authenticated:
        if request.user.member_type == 'teacher':
            return redirect('faculty:teacherprofile')
        else:
            return redirect('student:studentprofile')
            
    if request.method == "POST":
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        if username and raw_password:
            try:
                user_obj = CustomUser.objects.get(username=username)
                print(user_obj, user_obj.check_password(raw_password), '##########')
                user = authenticate(request, username=username, password=raw_password)
                login(request, user)
                if user_obj.member_type == 'teacher':
                    return redirect('faculty:teacherprofile')
                else:
                    return redirect('student:studentprofile')
            except Exception as e:
                print(e)
                messages.error(request, message='Invalid Credentials !!!')
    return render(request, template_name='login.html')

@login_required
def logoutView(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect("homepage")