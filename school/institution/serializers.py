from rest_framework import serializers
#from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import User, Student, Tutor, Instructor, Course, Book, Meeting

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "pk",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "is_student",
            "is_tutor",
            "is_instructor",
        ]

    """def create(self, valpkated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)"""

class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Instructor
        fields = [
            "pk",
            "user",
        ]
        depth = 3

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=[
            "pk",
            "title",
            "num_pages",
            "isbn13",
            "color",
            "publish_date",
            "price",
        ]


class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(required=False)
    book = BookSerializer(required=False)
    class Meta:
        model = Course
        fields=[
            "pk",
            "course_code",
            "course_name",
            "instructor",
            "book",
        ]
        depth = 3


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer(required=False, many=True)
    class Meta:
        model = Student
        fields = [
            "pk",
            "user",
            "course",
        ]

        depth=3

class TutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course = CourseSerializer(required=False, many=True)
    class Meta:
        model =Tutor
        fields=[
            "pk",
            "user",
            "course"
        ]
        depth = 3

class MeetingSerializer(serializers.ModelSerializer):
    tutor=TutorSerializer(required=False)
    student=StudentSerializer(required=False, many=True)
    course=CourseSerializer(required=False)
    class Meta:
        model = Meeting
        fields=[
            "pk",
            "date",
            "meeting_type",
            "time_in",
            "time_out",
            "tutor",
            "student",
            "course",
        ]

        depth = 3

"""

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            "pk",
            "course_code",
            "course_name",
        ]

class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    courses = CourseSerializer(many = True, required=False)

    class Meta:
        model = Instructor
        fields =[
            "pk",
            "user",
            "courses",
        ]
    
    def create(self, validated_data):
        
        ##Overriding the default create method of the Model serializer.
        #:param validated_data: data containing all the details of instructor
        #:return: returns a successfully created instructor record
        
        user_data = validated_data.pop("user")
        user = User.Serializer.create(UserSerializer(), validated_data=user_data) 
        courses_data = validated_data.pop('courses')
        instructor = Instructor.objects.update_or_create(user=user)
        for course_data in courses_data:
            Course.objects.update_or_create(instructor=instructor, **course_data)

        return instructor


class InstructorListSerializer(serializers.ModelSerializer):


class BookSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Book
        fields=[
            "pk",
            "title",
            "num_pages",
            "isbn13",
            "color",
            "publish_date",
            "price",
            "courses",
        ]
        extra_kwargs = {
            "publish_date": {"required": False},
            "price": {"required": False},
            "color": {"required": False},
            "isbn13": {"required": False},
            "courses":{"required": False},
        }




class StudentSerializer(serializers.ModelSerializer):
    
    #A student serializer to return the student details
    

    user = UserSerializer(required=True)
    course = CourseSerializer(required=True, many=True)

    class Meta:
        model = Student
        fields = [
            "user",
            "course",
        ]
    
    def create(self, validated_data):
        
        ##Overriding the default create method of the Model serializer.
        #:param validated_data: data containing all the details of instructor
        #:return: returns a successfully created instructor record
        
        user_data = validated_data.pop("user")
        user = User.Serializer.create(UserSerializer(), validated_data=user_data)
        student, created = Student.objects.update_or_create(user=user, course=)

        return student


class MeetingSerializer(serializers.ModelSerializer):
"""