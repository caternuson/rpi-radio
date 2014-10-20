#!/usr/bin/python
#===============================================================================
# radio_weather.py
#
# For use with rpi-radio. Show current weather conditions.
#   LED 8x8 matrix display = icon of current condition
#   7 segment display      = current temp in deg F
#
# 2014-10-20
# Carter Nelson
#===============================================================================
import sys
import httplib
from xml.dom.minidom import parseString
from Adafruit_LED_Backpack import Matrix8x8, SevenSegment
import os
os.chdir('/home/pi/rpi-radio')
from led8x8icons import LED8x8_ICONS

#------------------------------------
# set up
#------------------------------------
NOAA_URL = "w1.weather.gov"
REQUEST = r"/xml/current_obs/KBFI.xml"

matrix = Matrix8x8.Matrix8x8(address=0x70)
segment = SevenSegment.SevenSegment(address=0x74)

matrix.begin()
segment.begin()

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
# do this if anything bad happens
#------------------------------------
def giveup():
    global matrix, segment
    set_raw64(LED8x8_ICONS['UNKNOWN'])
    segment.print_number_str('DEAD')
    segment.write_display()
    print "something happened...giving up...."
    sys.exit(1)

#------------------------------------
# make the request
#------------------------------------
try:
  conn = httplib.HTTPConnection(NOAA_URL)
  conn.request("GET", REQUEST)
  resp = conn.getresponse()
  data = resp.read()
except:
  giveup()

#------------------------------------
# parse the XML response into the DOM
#------------------------------------
dom = parseString(data)

#------------------------------------
# get weather and temperature
#------------------------------------
weather = dom.getElementsByTagName("weather")[0].firstChild.nodeValue
temp = int(round(float(dom.getElementsByTagName("temp_f")[0].firstChild.nodeValue)))

print weather
print temp

#------------------------------------
# set LED 8x8 with weather icon
#------------------------------------
if "SUNNY" in weather.encode('ascii','ignore').upper():
    set_raw64(LED8x8_ICONS['SUNNY'])
elif "RAIN" in weather.encode('ascii','ignore').upper():
    set_raw64(LED8x8_ICONS['RAIN'])
elif "CLOUD" in weather.encode('ascii','ignore').upper():
    set_raw64(LED8x8_ICONS['CLOUD'])
elif "SHOWERS" in weather.encode('ascii','ignore').upper():
    set_raw64(LED8x8_ICONS['SHOWERS'])
else:
    set_raw64(LED8x8_ICONS['UNKNOWN'])

#------------------------------------
# set 7 segment with temperature
#------------------------------------
segment.print_number_str("{0}F".format(temp))
segment.write_display()