#!/usr/bin/python
#===============================================================================
# flickr_count_disp.py
#
# Show an icon and the number of files.
#
# 2014-10-20
# Carter Nelson
#===============================================================================
import piradio
import led8x8bico_icons as ICONS

pr = piradio.PiRadio()

#------------------------------------
# get count and display it
#------------------------------------
with open('/home/pi/flickr_count','r') as f:
    N = int(f.readline())
pr.disp_text("%4i" % N)
pr.disp_bitmap(ICONS.CAMERA)