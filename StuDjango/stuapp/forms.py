#!/usr/bin/env python3
# coding=utf-8
# title          :forms.py
# description    :TopicForms
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/9/12 19:52
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
