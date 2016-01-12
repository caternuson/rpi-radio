rpi-radio
=========

Python code for Raspberry Pi based internet radio and music server.

This was orignally going to be a stand alone music player with its own amp and speaker. However, found it easier to just attach it to existing stereo and run it headless using mpd. Added a 8x8 bicolor and alpha numeric matrix to give it some fun display capabilities.

Hardware Summary
================
* Raspberry Pi B+
* USB WiFi module https://www.adafruit.com/products/814 
* USB audio adapter https://www.adafruit.com/products/147
* Bicolor 8x8 LED matrix https://www.adafruit.com/products/902
* 7 Segment LED display https://www.adafruit.com/products/878
* 
Software Summary
================
* piradio.py = defines a class with methods for controlling the hardware of the piradio box
* show_time.py = displays a clock icon and current time
* radio_weather.py = displays current temperature and a weather icon
* music_count_disp.py = something to do with music sharing
* display_something.py = run from cron to rotate through various display programs
* led8x8bico_icons.py = defines various icons for the bicolor display
* led7seg_alpha.py = defines various characters for the 7 segment display
