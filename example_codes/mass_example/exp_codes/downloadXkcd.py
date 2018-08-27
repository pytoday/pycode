#!/usr/bin/env python3
# coding=utf-8
# title          :downloadXkcd.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/6/1 18:21:53
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import os
import bs4
import requests

url = 'https://xkcd.com'
os.makedirs('E:\\Fun\\Pics\\xkcd', exist_ok=True)
imgDir = 'E:\\Fun\\Pics\\xkcd'

while not url.endswith('#'):
    #TODO: Download the page.
    print('Downloading page %s ....' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    #TODO: Find the url of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        #TODO: Download the image.
        print('Downloading image %s ....' % comicUrl)
        imgRes = requests.get(comicUrl)
        res.raise_for_status()

    #TODO: Save image to dirs.
    imgFile = open(os.path.join(imgDir, os.path.basename(comicUrl)), 'wb')
    for chunk in  imgRes.iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()

    #TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')