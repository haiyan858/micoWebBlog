#!/usr/bin/env python
# encoding:utf-8

# Create_Author: cuihaiyan
# Create_time: 2018/8/28 18:08
# Desc:  

from django.conf.urls import url
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^login/$',views.user_login,name="user_login"), # 自定义的登陆
    url(r'^login/$', auth_views.login, name='user_login'),  # django 的内置登陆
    url(r'^new-login/$', auth_views.login, {"template_name": "account/login.html"}),
    # url(r'^logout/$',auth_views.logout,name='user_logout'),
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"}, name='user_logout'),
    url(r'^register/$', views.register, name="user_register"),
    url(r'^password-change/$', auth_views.password_change, {"post_change_redirect":"/account/password-change-done"},name="password_change"),
    url(r'^password-change-done/$', auth_views.password_change_done,name="password_change_done"),
    url(r'^password-reset/$',auth_views.password_reset,
        {"template_name":"account/password_reset_form.html",
        "email_template_name":"account/password_reset_email.html",
        "subject_template_name":'account/password_reset_subject.txt',
        "post_reset_redirect":"account/password_reset_done"},name="password_reset"),
    url(r'^password-reset-done/$',auth_views.password_reset_done,{"template_name": "account/password_reset_done.html"}, name='password_reset_done'),
    url(r'password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,
        {"template_name": "account/password_reset_confirm.html",
         "post_reset_redirect":"/account/password-reset-complete"},name='password_reset_confirm'),
    url(r'^password-reset-complete/$',auth_views.password_reset_complete,{"template":"account/password_reset_complete.html"},name="password_reset_complete")

]
# post_reset_redirect
# password_reset_complete

# template_name='registration/password_reset_form.html',
# email_template_name='registration/password_reset_email.html',
# subject_template_name='registration/password_reset_subject.txt',
# password_reset_form=PasswordResetForm,
# token_generator=default_token_generator,
# post_reset_redirect=None,
# from_email=None,
# extra_context=None,
# html_email_template_name=None,
# extra_email_context=None):
# if post_reset_redirect is None: