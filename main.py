import ntptime
import utime

print ('Sync timeserver..')
ntptime.time()
utime.sleep(3)
print ('Update RTC Time')
ntptime.settime()
led.off()

#-- Run loop --
execfile('prayer.py')
