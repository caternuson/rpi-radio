#!/usr/bin/python
#===============================================================================
# show_time.py
#
# For use with rpi-radio. Show current time and clock face icon.
#
# 2015-07-21
# Carter Nelson
#===============================================================================
import piradio
import led8x8bico_icons as ICONS

pr = piradio.PiRadio()
pr.disp_time()
pr.disp_bitmap(ICONS.CLOCK_FACE)