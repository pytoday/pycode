#!/usr/bin/env python3
# coding=utf-8
# title          :urls.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/9/7 6:33
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


from django.conf.urls import url
from stuapp import views


urlpatterns = [
    # main page
    url(r'^$', views.index, name='index'),
    # all topics
    url(r'^topics/$', views.topics, name='topics'),
    url(r'topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    url(r'.*', views.nothing, name='nothing')
]
