#!/usr/bin/env python3
# coding=utf-8
# title          : setup.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/8/15 17:28
# email          : jackietsui72@gmail.com
# notes          : c extension
# ==================================================

# Import the module needed to run the script
from distutils.core import setup, Extension


MOD = 'Extest'
setup(name=MOD, ext_modules=[Extension(MOD, sources=['Extest.c'])])
