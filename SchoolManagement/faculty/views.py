from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Teacher, Class, Subject
from PIL import Image
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from faculty.models import *
# Create your views here.
def teacherRegister(request):
    template_name = 'teacher-register.html'
    user_obj = None
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        mobileno = request.POST.get('mobileno')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        profile_pic = request.FILES['profilepic']
        member_type = request.POST.get('membertype')

        if first_name and last_name:
            if len(first_name)<3 and len(last_name)<3:
                messages.error(request, "first name and last name must be greater than 3 charecters.")
                return redirect("register")


        if profile_pic:
            img = Image.open(profile_pic)
            width = img.width
            height = img.height
            print(img.format)
            if width % height != 0:
                messages.error(request, "Images must be square in shape")
                return redirect("register")
            if width > 301 and height > 301:
                messages.error(
                    request, "Image size must be less than 301x301 in pixels"
                )
                return redirect("register")
        if profile_pic is None:
            print("None.........")
            messages.error(request, message="Choose a Profile Pic ")
            return redirect("register")

        if member_type == 'none':
            messages.error(request, message="Choose member type ")
            return redirect("register")
        if len(mobileno) != 10:
            messages.error(request, message="Please enter valid mobile number.")
            return redirect("register")
        if password != conf_password:
            messages.error(request, message="password mismatched ...")
            return redirect("register")
        try:
            validate_password(password)
        except Exception as e:
            messages.error(request, message=f"{e}")
            return redirect("register")
        try:
            user_obj = CustomUser(username=username, first_name=first_name, last_name=last_name, email=email, profile_img=profile_pic, member_type=member_type)
            user_obj.set_password(raw_password=password)
            user_obj.save()
        except Exception as e:
            print(e)
            messages.error(request, message="Either username or email has been taken.")
        try:
            if user_obj is not None and member_type=='teacher':
                Teacher.objects.create(teacher=user_obj, contact_no=mobileno)
                messages.success(request, message="Registered successfully.")
        except Exception as e:
            print(e)
            messages.error(request, message="Something went wrong.")

    return render(request, template_name=template_name)

@login_required
def teacherProfile(request):
    teacher_obj = Teacher.objects.get(teacher = request.user)
    class_obj = Class.objects.filter(teacher=teacher_obj)
    print(class_obj)
    context = {
        'teacher':teacher_obj,
        'classes':class_obj,
    }
    return render(request, template_name='profile_teacher.html', context=context) 