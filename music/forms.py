from django import forms

class Login(forms.Form):
    userName = forms.CharField(label="username", max_length=20)
    password = forms.CharField(label="password", max_length=20)
    captcha = forms.CharField(label="captcha", max_length=20)
