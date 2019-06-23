# prayerclock
Hardward:
- ESP32 DOIT ESP32 DEVKIT/ESP-WROOM-32
- MP3-TF-16P + SD Card 
- Max7219 Led Matrix Module X 4

Installation
1. Install Micro Python to ESP32

#Preperation
    - USB driver for ESP32 - CP2102            
    - Python and PIP
    - esptool.py - <a href="https://github.com/espressif/esptool">Tutorial</a>
    - ampy - <a href="https://github.com/pycampers/ampy">Tutorial</a>
    - micropython firmware - <a href="http://micropython.org/download">Download</a>

#Erase_flash
    esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash
#ESP32
    esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART write_flash -z 0x1000 *.bin

<p align="center">
  <img src="prayerclock.png" width="550" title="Prayer Clock Schemetic Diagram">
</p>