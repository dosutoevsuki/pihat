#!/usr/bin/env python
# this script will define colors for a scrolling mesage on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colors
white = (255, 255, 255)
raspberry = (255, 0, 125)

speed = 0.3

message = "Hello World!"

sense.show_message(message, speed, text_colour=raspberry, back_colour=white)

sense.clear()
