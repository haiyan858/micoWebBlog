#!/usr/bin/env python
# encoding:utf-8

# Create_Author: cuihaiyan
# Create_time: 2018/8/28 18:12
# Desc:  

from django import forms

from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationFrom(forms.ModelForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    # 内部类
    class Meta:
        model = User
        fields = ("username","email")
    # clean_ + 属性名称 ，调用is_valid() 方法时，会执行这个函数
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords do not match.")
        return cd["password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=("phone","birth")


