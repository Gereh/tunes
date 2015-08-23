#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField
from django.forms import ModelForm
from .models import User


class Login(forms.Form):
    username = forms.CharField(label="username", max_length=20)
    password = forms.CharField(label="password", max_length=20, widget=forms.PasswordInput)
    captcha = CaptchaField()

    username.widget.attrs['placeholder'] = 'نام کاربری'
    password.widget.attrs['placeholder'] = 'رمز عبور'
    captcha.widget.attrs['placeholder'] = 'کد امنیتی'


class Register(ModelForm):
    password2 = forms.CharField(max_length=25)
    captcha = CaptchaField(error_messages={'invalid':'کد امنیتی اشتباه می باشد'})
    password2.widget.attrs['required']= 'required'
    captcha.widget.attrs['required']='کد امنیتی را وارد کنید'
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password']
        error_messages = {
            'username': {'required':'نام کاربری را وارد کنید'},
            'email': {'required':'ایمیل را وارد کنید'
                     ,'invalid':'ایمیل صحیح نمی باشد'},
            'name': {'required': 'نامتان را وارد کنید'},
            'password': {'required': 'پسورد را وارد کنید'}
        }


class ForgotPass(forms.Form):
    email = forms.EmailField()
    captcha = CaptchaField()
