
try:
  import usocket as socket
except:
  import socket

import esp
esp.osdebug(None)

import gc
gc.collect()

from machine import Pin
import network

#-- Status led ---
led = Pin(2, Pin.OUT)

#-- Wifi ---
f = open('wifi.txt')
s = f.read()
print (s);
ssid,password =  s.split(',')
f.close()

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#led.on() # on when wifi connected