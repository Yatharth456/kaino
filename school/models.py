from django.db import models
from django.contrib.auth.models import AbstractUser  
from .managers import UserManager

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    year_established = models.DateField()
    motto = models.CharField(max_length=255, null=True, blank=True)
    principal_name = models.CharField(max_length=124, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    website_url = models.URLField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True,blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=124, null=True, blank=True)
    country = models.CharField(max_length=124, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    cover = models.ImageField(upload_to='school_profile/', null=True, blank=True)
    slogan = models.CharField(max_length=255, null=True, blank=True)
    logo_img = models.ImageField(upload_to='school_logo/', null=True, blank=True)


class User(AbstractUser):
    Admin = 1
    Student = 2
    Teacher =3
    Parent = 4
    
    ROLE_CHOICES = (
        (Admin, 'Admin'), 
        (Student, 'Student'),
        (Teacher, 'Teacher'),
        (Parent, 'Parent'),
    )

    Male = 1
    Female = 2

    GENDER = (
        (Male, 'Male'),
        (Female, 'Female'),
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=250, blank=True, unique=True)
    email = models.EmailField(('email_address'), unique=True, max_length = 200)  
    password = models.CharField(max_length=100, blank=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    mobile_no = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=512, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    profile_img = models.ImageField(upload_to="profile", height_field=None, width_field=None, max_length=100, blank=True, default=None)
    remember_me = models.BooleanField(default=False)
    request_access = models.BooleanField(default=False)


    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    objects = UserManager()


class Session(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return "From " + str(self.start_year) + " to " + str(self.end_year)


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    date_of_joining = models.DateField()
    experience = models.IntegerField()

class Lession(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    summery = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(User ,on_delete=models.CASCADE, null=True, blank=True)
    students = models.ManyToManyField(Student,)

    def __str__(self):
        return self.title
    

class RollCall(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=False)


class AccessRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


# class Attendance(models.Model):
#     session = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
#     subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
#     date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class AttendanceReport(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
#     attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
#     status = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class LeaveReport(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     repoter = models.ForeignKey(User, on_delete=models.CASCADE)
#     # date = models.CharField(max_length=60)
#     message = models.TextField()
#     status = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     # start_year = models.DateField()
#     # end_year = models.DateField()


# # class LeaveReportTeacher(models.Model):
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     date = models.CharField(max_length=60)
# #     message = models.TextField()
# #     status = models.BooleanField(default=False)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)


# class StudentResult(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     test = models.FloatField(default=0)
#     exam = models.FloatField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     #marks