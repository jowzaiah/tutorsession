from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.enums import Choices
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False, help_text="This indicates if the user is a student or not")
    is_instructor = models.BooleanField(default=False, help_text="This indicates if the user is an isntructor or not")
    is_tutor = models.BooleanField(default=False, help_text="This indicates if the user is a tutor or not")

    def __str__(self):
        tag_1="" 
        tag_2=""
        if self.is_student == True:
            tag_1 = "student"
        if self.is_tutor == True:
            tag_2 = "tutor"
        elif self.is_instructor == True:
            tag_2 = "instructor"
        return f"{tag_1} {tag_2} {self.username}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    course = models.ManyToManyField('Course')

    def __str__(self):
        return f"{self.user}"

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.user}"

class Book(models.Model):
    title =models.CharField(max_length=255, null=True, blank=False)
    num_pages = models.IntegerField(default=0, null=True, blank=False)
    isbn13= models.CharField(max_length=13, blank=True, null=True)
    color = models.CharField(max_length=32, blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=4,blank=True,null=True)
    
    def __str__(self):
        return self.title

class Course(models.Model):

    COURSE_TYPE=(
        ('College Algebra', 'College Algebra'),
        ('Calculus', 'Calculus'),
        ('Plane Trigonometry', 'Plane Trigonometry'),
        ('Statistics', 'Statistics'),
        ('Functions And Modeling', 'Functions And Modeling')
    )

    course_code = models.CharField(max_length=7, null=True, blank=False)
    course_name = models.CharField(max_length=100, null=True, blank=False, choices=COURSE_TYPE)
    instructor = models.ForeignKey(Instructor, null=True, related_name='courses', on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, related_name='courses', on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.course_code} {self.course_name}"


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    course= models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.user}"

class Meeting(models.Model):

    MEETING_TYPE=(
        ('In Person', 'In Person'),
        ('Zoom', 'Zoom')
    )
    
    date = models.DateField(null=True, blank=False)
    meeting_type = models.CharField(max_length=50, null=True, choices=MEETING_TYPE)
    time_in = models.DateTimeField(null=True, blank=False)
    time_out = models.DateTimeField(null=True, blank=False)
    tutor = models.ForeignKey(Tutor, null=True, on_delete= models.SET_NULL)
    student = models.ManyToManyField(Student)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"Meeting {self.id}"

    
