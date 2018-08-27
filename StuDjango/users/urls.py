#!/usr/bin/env python3
# coding=utf-8
# title          :urls.py
# description    :user app url pattern
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/9/14 13:53
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from django.conf.urls import url
from django.contrib.auth.views import login

from . import views


urlpatterns = [
    # login page
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register', views.register, name='register'),
]
