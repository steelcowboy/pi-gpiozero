#! /usr/bin/env python3

from gpiozero import *
from os import getloadavg
from time import sleep
import mypins

leds = []

for x in mypins.pins6:
    leds.append(LED(x))

def chooseLoadLevel(load):
    if load <= 0.25:
        return 1
    elif 0.25 < load <= 0.5:
        return 2
    elif 0.5 < load <= 0.75:
        return 3
    elif 0.75 < load <= 1:
        return 4
    elif 1 < load <= 1.25:
        return 5
    elif load > 1.25:
        return 6

while True:
    recentLoad = getloadavg()[0]
    numLEDs = chooseLoadLevel(recentLoad)
    if numLEDs == 6:
        for x in leds:
             x.blink()
    else:
        for y in range(0,len(leds)):
            if y < numLEDs:
                leds[y].on()
            else:
                leds[y].off()
    sleep(2)
	

    
