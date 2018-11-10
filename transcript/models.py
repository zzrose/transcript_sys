# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser
# Create your models here.


class Degree(models.Model):
    degree_id = models.CharField(max_length=9, verbose_name='Degree ID', blank=True, null=True)
    degree = models.CharField(max_length=20, choices= (('cs','COMPUTER SCIENCE'),('mac', 'MASTER OF APPLIED COMPUTING')), default='mac')

    class Meta:
        verbose_name = 'Degree'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.degree


class UserProfile(AbstractUser):
    student_num = models.CharField(max_length=9, verbose_name='Student ID', blank=True, null=True)
    birthday = models.DateField(verbose_name='Birthday', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male', 'Male'),('female', 'Female')), default='female')
    address = models.CharField(verbose_name='Address', max_length=100, blank=True, null=True)
    city = models.CharField(verbose_name='City', max_length=20, default='Windsor')
    province = models.CharField(max_length=20, verbose_name='Province', default='ON')
    zip_code = models.CharField(max_length=6, verbose_name='post code', blank=True, null=True )
    mobile = models.CharField(max_length=10, null=True, blank=True)
    enter_date = models.DateField(verbose_name='Enter Date', blank=True, null=True)
    degree = models.ForeignKey(Degree, verbose_name='Degree', on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'StudentInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Course(models.Model):
    course_name = models.CharField(max_length=20, verbose_name='course_name', blank=True, null=True)
    description = models.TextField(max_length=100, verbose_name='Description', blank=True, null=True)
    semester = models.CharField(max_length=20, choices=(('summer','Summer'),('fall','Fall'),('winter','Winter')), default='Fall')
    credit = models.CharField(max_length=40, verbose_name='Credit', blank=True, null=True)

    # user_name = models.ForeignKey(UserProfile,  verbose_name='user_name', on_delete=models.CASCADE, blank=True, null=True)
    # id = models.CharField(primary_key=True, max_length=4, blank=True, default='1')
    # grade = models.IntegerField(verbose_name='grade', blank=True, null=True)
    # unique_together = ('id', 'course_name')
    # python = models.CharField(verbose_name='Python', max_length=100, default='')
    # java = models.CharField(verbose_name='JAVA', max_length=100, default='')
    # c = models.CharField(verbose_name='C', max_length=100, default='')
    # c_plusplus = models.CharField(verbose_name='C++', max_length=100, default='')
    # db = models.CharField(verbose_name='DATABASE', max_length=100, default='')
    # algorithm = models.CharField(verbose_name='ALGORITHM', max_length=100, default='')
    class Meta:
        verbose_name = 'CourseInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course_name


class Grade(models.Model):
    student = models.ForeignKey(UserProfile, verbose_name="Student", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='Course',on_delete=models.CASCADE)
    grade = models.IntegerField(verbose_name='Grade', null=True, blank=True)

    class Meta:
        verbose_name = 'Grade Info'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student.username




