#!/usr/bin/env python3
# coding=utf-8
# title          :python_repos.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/8/29 21:45
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script

import requests


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
for num, key in enumerate(repo_dict.keys()):
    print("%d: %s" % (num, key))

print("\nSelected information about this repositories:")

for repo_dict in repo_dicts:
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Starts:", repo_dict['stargazers_count'])
    print("Repositories:", repo_dict['html_url'])
    print("Description:", repo_dict['description'])
