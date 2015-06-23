#!/usr/bin/python
#===============================================================================
# music_count_disp.py
#
# Show an icon and the number of files.
#
# 2014-10-20
# Carter Nelson
#===============================================================================
import piradio
from led8x8icons import LED8x8_ICONS

import os, os.path

pr = piradio.PiRadio()

#------------------------------------
# defines
#------------------------------------
MUSIC_DIR = "/var/www/music_in/"

#------------------------------------
# get file count
#------------------------------------
N = len([name for name in os.listdir(MUSIC_DIR) if os.path.isfile(MUSIC_DIR+name)])
print "Found {0} music file(s) in {1}".format(N,MUSIC_DIR)

#------------------------------------
# output to displays
#------------------------------------
pr.disp_text("{0}".format(N))
if (N==0):
    pr.disp_raw64(LED8x8_ICONS['BOX_FROWN'],2)
else:
    pr.disp_raw64(LED8x8_ICONS['BOX_SMILE'],1)