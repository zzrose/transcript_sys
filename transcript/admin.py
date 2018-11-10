from django.contrib import admin

import xadmin
from xadmin import views
from .models import UserProfile, Course, Degree, Grade
# Register your models here.


class UserProfileAdmin(object):
    search_fields = ['student_num', 'first name', 'last name']  # 搜索框，能作用的属性有什么
    list_filter = ['student_num', 'first name', 'last name', 'mobile']  # 筛选功能
    list_display = ['student_num', 'first_name', 'last_name', 'gender', 'address', 'city', 'province', 'zip_code',
                    'mobile', 'enter_date', 'degree', 'major']


#xadmin.site.register(UserProfile,UserProfileAdmin)


class CourseAdmin(object):
    search_fields = ['course_name', 'description', 'semester', 'credit']  # 搜索框，能作用的属性有什么
    list_filter = ['course_name', 'description', 'semester', 'credit']  # 筛选功能
    list_display = ['course_name', 'description', 'semester', 'credit']


xadmin.site.register(Course, CourseAdmin)


class DegreeAdmin(object):
    search_fields = ['degree_id', 'degree']  # 搜索框，能作用的属性有什么
    list_filter = ['degree_id', 'degree']  # 筛选功能
    list_display = ['degree_id', 'degree']


xadmin.site.register(Degree, DegreeAdmin)


class GradeAdmin(object):
    search_fields = ['student', 'course', 'grade']  # 搜索框，能作用的属性有什么
    list_filter = ['student', 'course__course_name', 'grade']  # 筛选功能
    list_display = ['student', 'course', 'grade']

xadmin.site.register(Grade, GradeAdmin)
