import http_client
import scanplayer
import max7219
from machine import Pin, SPI
import utime
import time

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 4)

# function Show clock 
def showclock(hour,minute):
    if (hour < 10):
        h1 = '0'
        h2 = str(hour)
    else:
        h = str(hour)
        h1 = h[0]
        h2 = h[1]
    
    if (minute < 10):
        m1 = '0'
        m2 = str(minute)
    else:
        m = str(minute)
        m1 = m[0]
        m2 = m[1]

    display.fill(0)
    display.pixel(16,3,1)
    display.pixel(16,5,1)
    display.text(h1,0,1,1)
    display.text(h2,7,1,1)
    display.text(m1,17,1,1)
    display.text(m2,24,1,1)
    display.show()

#-- Show next pray
def show_nextpray(hour,minute,ptime):
    for t in ptime:
        (h,m) = t.split(':')
        if  hour*60+minute <= int(h)*60+int(m)  :
            showclock(int(h),int(m))
            return True

#- function format time
def tf(t):
    if len(str(t)) == 1:
        return '0'+str(t)
    else:
        return str(t)

#- function get pray time
def getPlayerTime():
    #url = "http://api.pray.zone/v2/times/today.json?city=bangkok&school=5"
    url = "http://www.muslimthaipost.com/prayertimes/solaat.php?TYcHwyNDtkQVVUTzttQVVUTzt5QVVUTzsxMzA7MTY2OyMwMDAwRkY7IzAwMDBGRjsjRkZGRkZGOyNGRkZGRkY7I0ZGRkZGRjsjRkZGRkZGOyNGRkZGRkY7IzAwMDAwMDsjMDAwMDAwOyMwMDAwMDA7Ozs7Ozs7Ozs7Ozs7Ozs7OzI7MDswO3BkfFBTOzE7OzE7MS4yO2M2Mw=="
    r = http_client.get(url)
    html = r.text
    line  = html.split('<font color=#000000>')

    return [line[3].split(' ')[0],line[5].split(' ')[0],line[7].split(' ')[0],line[9].split(' ')[0],line[11].split(' ')[0]]


# --- Main ---
prv_tick = utime.ticks_ms()
interval = 1*1000

#clear screen
display.fill(0)
display.show()
(year,month,day,hour,minute,second,week,days) = utime.localtime(utime.time()+3600*7)
print (year,month,day,hour,minute,second)        
showclock(hour,minute)

#----- MP3 ----------#
print("start prayer")
player = scanplayer.ScanPlayer()

ptime  =  getPlayerTime()
#ptime  = ['09:22','09:23','09:24','13:40','13:41']
print (ptime)
ps = [True,True,True,True,True,True]
ctime = ''
while True:        
    cur_tick = utime.ticks_ms()
    if cur_tick - prv_tick > interval : 
        prv_tick =cur_tick
        (year,month,day,hour,minute,second,week,days) = utime.localtime(utime.time()+3600*7)
        print (year,month,day,hour,minute,second)        
        if second == 0:
            showclock(hour,minute)  
            ctime =  tf(hour)+':'+tf(minute)
            print('show clock ->',ctime)
            if ptime[0] == ctime and ps[0]:
                ps[0] = False
                player.play(10,1)
                print ("**** Play #1")
            elif ptime[1] == ctime and ps[1]:
                ps[1] = False
                player.play(10,2)
                print ("**** Play #2")
            elif ptime[2] == ctime and ps[2]:
                ps[2] = False
                player.play(10,2)
                print ("**** Play #2")
            elif ptime[3] == ctime and ps[3]:
                ps[3] = False
                player.play(10,2)
                print ("**** Play #2")
            elif ptime[4] == ctime and ps[4]:
                ps[4] = False
                player.play(10,2)
                print ("**** Play #2")
            
            # Update prayer time
            elif ctime == '01:30' and ps[5]:
                print ('Sync timeserver..')
                ntptime.time()
                utime.sleep(3)
                print ('Update RTC Time')
                ntptime.settime()
                ps = [True,True,True,True,True,True]
                ps[5] = False
                ptime  =  getPlayerTime()
                #ptime  = ['15:00','13:38','13:39','13:40','13:41']
                print (ptime)
        elif second == 55:
            show_nextpray(hour,minute,ptime)

     
    

print ('*** Exit ****')