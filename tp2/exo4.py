from microbit import *

i2c.init(freq=100000, sda=pin20, scl=pin19)
addresses = i2c.scan()

for addresse in addresses:
    print(i2c.read(addresse, 7))