#!/usr/bin/python
#===============================================================================
# display_something.py
#
# Display something based on whatever gets programmed here.
#
# 2014-10-27
# Carter Nelson
#===============================================================================
import os, os.path

MUSIC_DIR = "/var/www/music_in/"
SUDOPY="sudo -E PYTHONPATH=$PYTHONPATH python "
LASTRUN = "/tmp/lastrun"

PROGRAMS = [
    "/home/pi/rpi-radio/music_count_disp.py",
    "/home/pi/rpi-radio/radio_weather.py",
    "/home/pi/rpi-radio/show_time.py",
    "/home/pi/rpi-radio/reece_chat_disp.py",
    "/home/pi/rpi-radio/flickr_count_disp.py" ,
]

#================================================
# MAIN
#================================================
# simple rotation
N = 0
try:
    with open(LASTRUN,'r') as FILE:
        N = int(FILE.readline().splitlines()[0])
except IOError:
    # meh, do nothing, just let it be 0
    pass
N += 1
if N >= len(PROGRAMS):
    N = 0
with open(LASTRUN,'w') as FILE:
    FILE.write('%i' % N)
os.system(SUDOPY+PROGRAMS[N])
