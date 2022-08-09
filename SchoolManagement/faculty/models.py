from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser): 
    MEMBER_TYPE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    profile_img = models.ImageField(default='user.png', upload_to='uploads/')
    member_type = models.CharField(choices=MEMBER_TYPE_CHOICES, max_length=80)
    # EMAIL_FIELD = email
    def __str__(self):
        return self.username

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=50)
    def __str__(self):
        return self.subject_name
    
class Teacher(models.Model):
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    teacher_room = models.CharField(max_length=100)
    core_subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, null=True)
    # onetoone field for address
    contact_no = models.CharField(max_length=10)
    # one field for bank accout number

    def __str__(self):
        return self.teacher.username
    

class Class(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField(editable=True, blank=True, null=True)

    def __str__(self):
        return self.subject.subject_name
    