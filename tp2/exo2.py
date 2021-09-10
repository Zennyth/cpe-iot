from microbit import *
import neopixel
from random import randint

# Setup the Neopixel strip on pin0
NUMBER_OF_LED = 2
np = neopixel.NeoPixel(pin0, NUMBER_OF_LED)

colors = {
    "blue": (0,0,60),
    "white": (60,60,60),
    "red": (60,0,0),
}

def change_color(color, sleep_time = 250):
    for pixel_id in range(0, len(np)):
        np[pixel_id] = colors[color]
        np.show()
        sleep(sleep_time / 5) #OLLA
    sleep(sleep_time)

while True:
    change_color("blue")
    change_color("white")
    change_color("red")