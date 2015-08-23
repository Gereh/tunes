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

    username.widget.attrs['required']= 'required'
    username.widget.attrs['placeholder'] = 'نام کاربری'

    password.widget.attrs['required']= 'required'
    password.widget.attrs['placeholder'] = 'رمز عبور'

    captcha.widget.attrs['required']= 'required'
    captcha.widget.attrs['placeholder'] = 'کد امنیتی'



class Register(ModelForm):
    password2 = forms.CharField(max_length=25)
    captcha = CaptchaField(error_messages={'invalid':'کد امنیتی اشتباه می باشد'})

    password2.widget.attrs['required']= 'required'
    password2.widget.attrs['placeholder']= 'پسورد'

    captcha.widget.attrs['required']='required'
    captcha.widget.attrs['placeholder']='کد امنیتی'

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
            'email': forms.TextInput(attrs={'placeholder': 'ایمیل'}),
            'name': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}),
            'password': forms.TextInput(attrs={'placeholder': 'رمز عبور'})
        }
        error_messages = {
            'email': {'invalid':'ایمیل صحیح نمی باشد'}
        }


class ForgotPass(forms.Form):
    email = forms.EmailField()
    captcha = CaptchaField()

    email.widget.attrs['required']= 'required'
    email.widget.attrs['placeholder']= 'ایمیل'

    captcha.widget.attrs['required']= 'required'
    captcha.widget.attrs['placeholder']= 'کد امنیتی'


