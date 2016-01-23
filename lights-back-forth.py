#! /usr/bin/env python3

from gpiozero import LED
import time

# List of which pins the LEDs are attached to,
# with a separate empty list for LED "objects"
pins = [26, 19, 13, 6, 21, 20] 
leds = []

# This makes a list of LED objects, so that
# we can loop through it later and blink each
# one following an order

for pin in pins:
    leds.append(LED(pin))

# Finally, we need to teach Python what it means
# to blink and LED

def blinkLED(light):
    light.on()
    time.sleep(0.1)
    light.off()

for led in leds:
    if led.is_lit:
        led.off()

while True:
    for led in leds:
        blinkLED(led)

    for led in reversed(leds):
        blinkLED(led)


