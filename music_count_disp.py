#!/usr/bin/python
#===============================================================================
# music_count_disp.py
#
# Show an icon and the number of files.
#
# 2014-10-20
# Carter Nelson
#===============================================================================
from Adafruit_LED_Backpack import Matrix8x8, SevenSegment
import os, os.path
from led8x8icons import LED8x8_ICONS

matrix = Matrix8x8.Matrix8x8(address=0x70)
segment = SevenSegment.SevenSegment(address=0x74)

#------------------------------------
# defines
#------------------------------------
MUSIC_DIR = "/var/www/music_in/"
BRIGHTNESS = 5  # 0-15

#------------------------------------
# set up displays
#------------------------------------
def setup_displays():
    matrix.begin()
    matrix.set_brightness(BRIGHTNESS)
    segment.begin()
    segment.set_brightness(BRIGHTNESS)
    
#------------------------------------
# set 8x8 matrix based on 64 bit value
#------------------------------------    
def set_raw64(value):
    global matrix
    matrix.clear()
    for y in [0, 1, 2, 3, 4, 5, 6, 7]:
        row_byte = value>>(8*y)
        for x in [0, 1, 2, 3, 4, 5, 6, 7]:
            pixel_bit = row_byte>>x&1 
            matrix.set_pixel(x,y,pixel_bit) 
    matrix.write_display()

#------------------------------------
# get file count
#------------------------------------
N = len([name for name in os.listdir(MUSIC_DIR) if os.path.isfile(MUSIC_DIR+name)])
print "Found {0} music file(s) in {1}".format(N,MUSIC_DIR)

#------------------------------------
# output to displays
#------------------------------------
setup_displays()
segment.print_number_str("{0}".format(N))
segment.write_display()
if (N==0):
    set_raw64(LED8x8_ICONS['BOX_FROWN'])
else:
    set_raw64(LED8x8_ICONS['BOX_SMILE'])