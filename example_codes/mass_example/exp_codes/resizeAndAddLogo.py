#!/usr/bin/env python3
# coding=utf-8
# title          :resizeAndAddLogo.py
# description    :Resize all images in current working directory to fit in a 300*300 square, and add catlog.png to image
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/7/19 4:30
# email          :jackietsui72@gmail.com
# notes          :Usage: resizeAndAddLogo.py /path/to/workdirectory /path/to/logo.png
# ==================================================

# Import the module needed to run the script
import os
import sys
from PIL import Image

if len(sys.argv) < 3:
    print('Parameter less than 2, exiting...')
    exit(1)

SQUARE_FIT_SIZE = 300
WORK_DIRECTORY = sys.argv[1]
LOGO_FILENAME = sys.argv[2]
WITH_LOG_DIR = os.path.join(WORK_DIRECTORY, 'withlogos')

logoIm = Image.open(LOGO_FILENAME)
cropIm = logoIm.crop((533, 30, 719, 193))
logoWidth, logoHeight = cropIm.size
os.makedirs(WITH_LOG_DIR, exist_ok=True)
os.chdir(WORK_DIRECTORY)

# TODO: Loop over all files in the working directory.
for filename in os.listdir(WORK_DIRECTORY):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == os.path.basename(LOGO_FILENAME):
        continue
    im = Image.open(filename)
    imWidth, imHeight = im.size

    # TODO: Check if image needs to be resized.
    if imWidth > SQUARE_FIT_SIZE and imHeight > SQUARE_FIT_SIZE:
        # TODO: Calculate the new width and heigh to resize to.
        if imWidth > imHeight:
            imWidth = SQUARE_FIT_SIZE
            imHeight = int((SQUARE_FIT_SIZE/imWidth) * imHeight)
        else:
            imHeight = SQUARE_FIT_SIZE
            imWidth = int((SQUARE_FIT_SIZE/imHeight) * imWidth)
        # TODO: Resize the image.
        print('Resizing %s ....' % filename)
        im = im.resize((imWidth, imHeight))

    # TODO: Add the logo on image.
    print('Adding logo to %s ...' % filename)
    im.paste(cropIm, (imWidth-logoWidth, imHeight-logoHeight), cropIm)
    # TODO: Save changes.
    im.save(os.path.join(WITH_LOG_DIR, filename))
