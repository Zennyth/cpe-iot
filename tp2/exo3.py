# dmesg find usb ttyACM0: USB ACM device
# minicom -D /dev/ttyACM0

from microbit import *
uart.init(115200)

to_send = "\n"
def add_to_send(string):
    global to_send
    to_send += string

while True:
    temp = "Tempearture : " + str(temperature())
    add_to_send(temp)
    uart.write("%c")
    uart.write(to_send)
    sleep(10000)