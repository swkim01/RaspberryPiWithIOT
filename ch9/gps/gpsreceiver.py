from gps import *
import threading
import time
import os

class GpsReceiver(threading.Thread):
    def __init__(self, lat=36.35, lon=127.385):
        threading.Thread.__init__(self)
        self.gpsd = gps("localhost", "2947")
        self.gpsd.stream(WATCH_ENABLE | WATCH_NEWSTYLE)
        self.running = True
        self.location = {'lat':lat, 'lon':lon, 'alt':0.0, 'speed':0.0}

    def run(self):
        try:
            while self.running:
                data = self.gpsd.next()
                if data['class'] == 'TPV':
                    self.location["lat"] = getattr(data,'lat',self.location["lat"])
                    self.location["lon"] = getattr(data,'lon',self.location["lon"])
                    self.location["alt"] = getattr(data,'alt',self.location["alt"])
                    self.location["speed"] = getattr(data,'speed',self.location["speed"])
                time.sleep(1.0)
        except StopIteration:
            pass

    def getLocation(self):
        return self.location

if __name__ == '__main__':
    gpsr = GpsReceiver()
    try:
        gpsr.start()
        # gpsc now polls every .5 seconds for new data
        while True:
            # In the main thread, every 1 seconds print the current data
            os.system('clear')
            location = gpsr.getLocation()
            print '          GPS Data'
            print '--------------------------------'
            print 'latitude    ' , location["lat"]
            print 'longitude   ' , location["lon"]
            print 'altitude    ' , location["alt"]
            print 'speed       ' , location["speed"]
            time.sleep(1)

    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "\nKilling Thread..."
        gpsr.running = False
        gpsr.join() # wait for the thread to finish what it's doing
    print "Done.\nExiting."

