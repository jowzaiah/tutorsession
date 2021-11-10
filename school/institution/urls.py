from django.urls import path

from . import views

urlpatterns= [
    path("users/", views.UserList.as_view()), #this endpoint is used to List all users and Create new users, ie GET and POST
    path("users/<int:pk>", views.UserDetail.as_view()), # this endpoint is used to retrieve, update, and delete information about a particular user, ie GET, PUT, DELETE
    path("students/", views.StudentList.as_view()), #this endpoint is used to List all student users and Create new student users, ie GET and POST
    path("students/<int:pk>", views.StudentDetail.as_view()), #this endpoint is used to retrieve, update, and delete information about a particular student user, ie GET, PUT, DELETE
    path("instructors/", views.InstructorList.as_view()), #this endpoint is used to List all instructor users and Create new instructor users, ie GET and POST
    path("instructors/<int:pk>", views.InstructorDetail.as_view()), #this endpoint is used to retrieve update and delete information about a particular instructor user, ie GET, PUT, DELETE
    path("courses/", views.CourseList.as_view()), #this endpoint is used to List all courses and Create new courses, ie GET and POST
    path("courses/<int:pk>", views.CourseDetail.as_view()), #this endpoint is used to retrieve update and delete information about a particular course, ie GET, PUT, DELETE
    path("tutors/", views.TutorList.as_view()), #this endpoint is used to List all tutor users and Create new tutor users, ie GET and POST
    path("tutors/<int:pk>", views.TutorDetail.as_view()), #this endpoint is used to retrieve update and delete information about a particular tutor user, ie GET, PUT, DELETE
    path("books/", views.BookList.as_view()), #this endpoint is used to List all books and Create new books, ie GET and POST
    path("books/<int:pk>", views.BookDetail.as_view()), #this endpoint is used to retrieve update and delete information about a particular book, ie GET, PUT, DELETE
    path("meetings/", views.MeetingList.as_view()), #this endpoint is used to List all meetings and Create new meetings, ie GET and POST
    path("meetings/<int:pk>", views.MeetingDetail.as_view()) #this endpoint is used to retrieve update and delete information about a particular meeting, ie GET, PUT, DELETE
]