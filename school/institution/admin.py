from django.contrib import admin
from .models import Book, Course, Instructor, Meeting, Student, Tutor, User

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Tutor)
admin.site.register(Meeting)

