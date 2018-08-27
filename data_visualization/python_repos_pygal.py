#!/usr/bin/env python3
# coding=utf-8
# title          :python_repos_pygal.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/29 21:45
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)
response_dic = r.json()
# print(response_dic.keys())
print("Total repositories:", response_dic['total_count'])

repo_dicts = response_dic['items']
print("Repositories returned:", len(repo_dicts))
repo_dict = repo_dicts[0]
print("Per repo dict has %s keys" % len(repo_dict.keys()))

names, stars, plot_dicts = [], [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        # 'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)


# print(plot_dicts)

# visualization
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
# let x label rotation 45
my_config.x_label_rotation = 45
# show_legend=False : instance show or ont show
my_config.show_legend = False
# set font size
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# truncate_label: x label length limit
my_config.truncate_label = 18
my_config.show_y_guides = False
my_config.width = 1000

# char = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
char = pygal.Bar(my_config, style=my_style)
char.title = "Most-Starred Python Projects on Github"
char.x_labels = names

char.add('', plot_dicts)
char.render_to_file('python_repos.svg')
