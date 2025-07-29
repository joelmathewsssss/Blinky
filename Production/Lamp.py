from machine import Pin
import time

# pins
LDR_PIN = 1            # photoresistor sense (digital)
LAMP_CTRL  = 20            # MOSFET gate

# setup
sensor = Pin(LDR_PIN, Pin.IN)         # using external pull‑up
lamp   = Pin(LAMP_CTRL, Pin.OUT)
# ensure lamp is off at start
lamp.value(0)

while True:
    # phototransistor conducts when LED is lit → pulls pin LOW
    if sensor.value() == 0:
        lamp.value(1)   # turn lamp on
    else:
        lamp.value(0)   # turn lamp off
    time.sleep(0.05)
