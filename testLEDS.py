#! /usr/bin/env python3

from gpiozero import *
from time import sleep
import mypins

leds = []

for x in mypins.pins6:
    leds.append(LED(x))

for x in leds:
    x.on()
    sleep(1)

for x in leds:
    x.off()

