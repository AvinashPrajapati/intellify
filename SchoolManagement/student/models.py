from django.db import models
from django.contrib.auth.models import User
from faculty.models import Teacher, Class, CustomUser
# Create your models here.

#student model inheriting faculty's CustomUser model which is the current Auth model
class Student(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # one to one field because one user -> will be teacher or student.
    dob = models.DateField(editable=True, null=True)
    contact_number = models.IntegerField()
    standard = models.CharField(max_length=3)
    stream = models.CharField(max_length=20, default="none")
    class_section = models.CharField(max_length=20, default='A')
    roll_number = models.IntegerField(null=True, blank=True)
    classes_taught = models.ForeignKey(Class)  # ForeignKey field because one student has many classes

    # address onetoonefield relation can be added
    # one bank_account_no field can also be added

    def __str__(self):
        return self.student.username

# in case if grade system required further
class Grade(models.Model):
    # considering id as assentment id and as primary key
    student_name = models.OneToOneField(Student, on_delete=models.CASCADE) 
    class_name = models.OneToOneField(Class, on_delete=models.CASCADE)
    assessment_date = models.DateField(editable=True)
    grade = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.grade 
    

    

