from django.db import models
from django.contrib.auth.models import User
from faculty.models import Teacher, Class, CustomUser
# Create your models here.
class Student(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob = models.DateField(editable=True, null=True)
    contact_number = models.IntegerField()
    standard = models.CharField(max_length=3)
    stream = models.CharField(max_length=20, default="none")
    class_section = models.CharField(max_length=20, default='A')
    roll_number = models.IntegerField(null=True, blank=True)
    classes_taught = models.ManyToManyField(Class)

    # address onetoonefield relation
    # one bank_account_no field

    def __str__(self):
        return self.student.username

class Grade(models.Model):
    # considering id as assentment id and as primary key
    student_name = models.OneToOneField(Student, on_delete=models.CASCADE) 
    class_name = models.OneToOneField(Class, on_delete=models.CASCADE)
    assessment_date = models.DateField(editable=True)
    grade = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.grade 
    

    

