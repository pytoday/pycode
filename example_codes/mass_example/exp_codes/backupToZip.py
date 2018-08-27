#!/usr/bin/env python3
# coding=utf-8
# title          :backupToZip.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/5/13 16:46:22
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

#Import the module needed to run the script
import os
import zipfile

#define function for zip
def backupZip(folder, dest):
    #get zipfile basename,  full path of source folder and destination.
    absFolder = os.path.abspath(folder)
    destFolder = os.path.abspath(dest)
    backupBasename = os.path.basename(folder)

    #check backuped zipfile is exist or not
    number = 1
    while True:
        destZipfile = os.path.join(destFolder, backupBasename + '_' + str(number) + '.zip')
        if not os.path.exists(destZipfile):
            break
        number += 1

    #open zipfile in destination folders
    print('Creating zipfile: %s ....' % (destZipfile))
    backupZipfile = zipfile.ZipFile(destZipfile, 'w')

    #add source folders and files to zipfile
    for foldername, subfolders, filenames in os.walk(absFolder):
        print('Adding files in %s ...' % (foldername))
        backupZipfile.write(foldername)

        for filename in filenames:
            backupZipfile.write(os.path.join(foldername, filename))
    backupZipfile.close()
    #all done. print backuped up info.
    print('All done.')

#call functions
backupZip('D:\\Codes\\pycode', 'E:\\backup')