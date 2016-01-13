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
import piradio
from led8x8icons import LED8x8_ICONS

import sys
import httplib
from xml.dom.minidom import parseString
import os
os.chdir('/home/pi/rpi-radio')

pr = piradio.PiRadio()

#------------------------------------
# defines
#------------------------------------
NOAA_URL = "w1.weather.gov"
REQUEST = "/xml/current_obs/KBFI.xml"
COLOR = 1 #   1=GREEN 2=RED 3=YELLOW
 
#------------------------------------
# do this if anything bad happens
#------------------------------------
def giveup():
    global pr
    pr.disp_raw64(LED8x8_ICONS['UNKNOWN'])
    pr.disp_text('DEAD')
    print "something happened...giving up...."
    sys.exit(1)

#------------------------------------
# make the request
#------------------------------------
try:
  conn = httplib.HTTPConnection(NOAA_URL)
  conn.request("GET", REQUEST, 
               headers={"User-agent":
                        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0"})
  resp = conn.getresponse()
  data = resp.read()
except:
  giveup()
  
#filename = "test.log"
#with open(filename,"w") as FILE:
#  FILE.write("-"*80+"\n")
#  FILE.write("URL = " + NOAA_URL + "\n")
#  FILE.write("REQUEST = " + REQUEST + "\n")
#  FILE.write("-"*80+"\n")
#  FILE.write(data)

#------------------------------------
# parse the XML response into the DOM
#------------------------------------
dom = parseString(data)

#------------------------------------
# get weather and temperature
#------------------------------------
weather = dom.getElementsByTagName("weather")[0].firstChild.nodeValue
temp = int(round(float(dom.getElementsByTagName("temp_f")[0].firstChild.nodeValue)))

print "%s, %3dF" % (weather, temp)

#------------------------------------
# set LED 8x8 with weather icon
#------------------------------------
if "SUNNY" in weather.encode('ascii','ignore').upper():
    pr.disp_raw64(LED8x8_ICONS['SUNNY'],COLOR)
elif "RAIN" in weather.encode('ascii','ignore').upper():
    pr.disp_raw64(LED8x8_ICONS['RAIN'],COLOR)
elif "CLOUD" in weather.encode('ascii','ignore').upper():
    pr.disp_raw64(LED8x8_ICONS['CLOUD'],COLOR)
elif "SHOWERS" in weather.encode('ascii','ignore').upper():
    pr.disp_raw64(LED8x8_ICONS['SHOWERS'],COLOR)
else:
    pr.disp_raw64(LED8x8_ICONS['UNKNOWN'],COLOR)

#------------------------------------
# set 7 segment with temperature
#------------------------------------
pr.disp_text("{0}F".format(temp))
