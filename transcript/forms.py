# _*_ coding: utf-8 _*_
__author__ = 'zzrose'
__date__ = '2018/11/7 11:33'
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)