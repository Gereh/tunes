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
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password']


class ForgotPass(forms.Form):
    email = forms.EmailField()
    captcha = CaptchaField()
