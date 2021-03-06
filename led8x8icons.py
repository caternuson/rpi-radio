#!/usr/bin/python
#===============================================================================
# led8x8icons.py
#
# Dictionary of LED 8x8 matrix icons as 64 bit values.
#
# Code snippet for computing value from bitmap:
#
#           BITMAP = [
#           [1, 1, 1, 1, 1, 1, 1, 1,],
#           [1, 1, 0, 0, 0, 0, 0, 1,],
#           [1, 0, 1, 0, 0, 0, 0, 1,],
#           [1, 0, 0, 1, 0, 0, 0, 1,],
#           [1, 0, 0, 0, 1, 0, 0, 1,],
#           [1, 0, 0, 0, 0, 1, 0, 1,],
#           [1, 0, 0, 0, 0, 0, 1, 1,],
#           [1, 0, 0, 0, 0, 0, 0, 1,],
#           ]
#           value = 0
#           for y,row in enumerate(BITMAP):
#               row_byte = 0
#               for x,bit in enumerate(row):
#                   row_byte += bit<<x    
#               value += row_byte<<(8*y)
#           print '0x'+format(value,'016x')
#
# Code snippet for setting individual LEDs on the display based on value:
#
#        def set_raw64(value):
#            led8x8matrix.clear()
#            for y in [0, 1, 2, 3, 4, 5, 6, 7]:
#                row_byte = value>>(8*y)
#                for x in [0, 1, 2, 3, 4, 5, 6, 7]:
#                    pixel_bit = row_byte>>x&1 
#                    led8x8matrix.set_pixel(x,y,pixel_bit) 
#            led8x8mmatrix.write_display() 
#
# 2014-10-20
# Carter Nelson
#==============================================================================
LED8x8_ICONS = { 
#---------------------------------------------------------
# misc
#---------------------------------------------------------
'ALL_ON'                            : 0xffffffffffffffff ,
'ALL_OFF'                           : 0x0000000000000000 ,
'UNKNOWN'                           : 0x00004438006c6c00 ,
'BOTTOM_ROW'                        : 0xff00000000000000 ,
'TOP_ROW'                           : 0x00000000000000ff , 
'LEFT_COL'                          : 0x0101010101010101 ,
'BOX'                               : 0xff818181818181ff ,
'XBOX'                              : 0xffc3a59999a5c3ff ,
'HEART1'                            : 0x001028448282926c ,
'BOX_SMILE'                         : 0xff8199a581a581ff ,
'BOX_FROWN'                         : 0xff81a59981a581ff ,
#---------------------------------------------------------
# weather
#---------------------------------------------------------
'SUNNY'                             : 0x9142183dbc184289 ,
'RAIN'                              : 0x55aa55aa55aa55aa ,
'CLOUD'                             : 0x00007e818999710e ,
'SHOWERS'                           : 0x152a7e818191710e ,
#---------------------------------------------------------
# digits
#---------------------------------------------------------
'0'                                 : 0x003c42464a52623c ,
'1'                                 : 0x003e0808080e0808 ,
'2'                                 : 0x007e02023c40403e ,
'3'                                 : 0x003e40403040403e ,
'4'                                 : 0x004040407e424242 ,
'5'                                 : 0x003e40403e02027e ,
'6'                                 : 0x003c42423e02027c ,
'7'                                 : 0x004040404042427e ,
'8'                                 : 0x003c42423c42423c , 
'9'                                 : 0x003c40407c42423c ,
#---------------------------------------------------------
# default
#---------------------------------------------------------
''                                 : 0x0000000000000000
}
