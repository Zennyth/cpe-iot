from microbit import *

leds = {
    "green": pin0,
    "orange": pin1,
    "red": pin2
}

ON = 1
OFF = 0

def change_state_led(led, state):
    led.write_digital(state)
    
def switch_led(led_on, sleep_time = 4000):
    for led in leds.values():
        to_state = OFF if led != led_on else ON
        change_state_led(led, to_state)
    sleep(sleep_time)

while True:
    switch_led(leds["red"])
    switch_led(leds["orange"], 2000)
    switch_led(leds["green"])
    switch_led(leds["orange"], 2000)