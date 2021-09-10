## Exo 3
from microbit import *
display.scroll("Hello, World!")

## Exo 4
from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll("PRESSED")
    else:
        display.scroll("")

## Exo 5
from microbit import *

while True:
    temp = temperature()
    if temp > 30:
        display.show("OULALA :" + str(temp))

## Exo 6 (compass)
from microbit import *

count = 0
prev = compass.get_x()
while True:
    if prev > 0 and compass.get_x() < 0:
        count += 1
    
    prev = compass.get_x()
    
    display.show(count)

## Exo 6 (accelerometre)
from microbit import *

count = 0
prev = accelerometer.get_x()
while True:
    if prev > 0 and accelerometer.get_x() < 0:
        count += 1
    
    prev = accelerometer.get_x()
    
    display.show(count)

## Exo 7
from microbit import *
# Start calibrating
compass.calibrate()
# Try to keep the needle pointed in (roughly) the correct direction
while True:
    sleep(100)
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])

