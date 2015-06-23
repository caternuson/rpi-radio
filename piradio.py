#!/usr/bin/python
#===========================================================================
# piradio.py
#
# Class to represent the pi radio box. Hardware:
#   * Raspberry Pi B+
#   * Adafruit 7 segment LED display
#   * Adafruit 8x8 bicolor LED matrix
#
# 2015-06-22
# Carter Nelson
#===========================================================================
from Adafruit_LED_Backpack import SevenSegment
from Adafruit_LED_Backpack import BicolorMatrix8x8
from led7seg_alpha import LED7SEG_ALPHA

class PiRadio():
    
    I2C_BUS = 1
    D7_ADDR = 0x74
    D8_ADDR = 0x70
    
    def __init__(self):
        self.d7 = SevenSegment.SevenSegment(address=self.D7_ADDR, busnum=self.I2C_BUS)
        self.d8 = BicolorMatrix8x8.BicolorMatrix8x8(address=self.D8_ADDR, busnum=self.I2C_BUS)
        
        self.d7.begin(); self.d7.set_brightness(1); self.d7.clear(); self.d7.write_display()
        self.d8.begin(); self.d8.set_brightness(1); self.d8.clear(); self.d8.write_display()
        
    def disp_bitmap(self, bitmap):
        self.d8.clear()
        for x,row in enumerate(bitmap):
            for y,c in enumerate(row):
                self.d8.set_pixel(x,7-y,c)
        self.d8.write_display()
        
    def disp_raw64(self, value, color=2):
        self.d8.clear()
        for y in xrange(8):
            row_byte = value>>(8*y)
            for x in xrange(8):
                pixel_bit = row_byte>>x&1 
                self.d8.set_pixel(y,7-x, color if pixel_bit else 0) 
        self.d8.write_display()
        
    def disp_text(self, text):
        self.d7.clear()
        for i,c in enumerate(text):
            if i>3:
                break
            self.d7.set_digit_raw(i, LED7SEG_ALPHA.get(c.upper(), 0x00))
        self.d7.write_display()

#===========================================================
# MAIN
#===========================================================
if __name__ == '__main__':
    print "I'm just a class, not a program."
