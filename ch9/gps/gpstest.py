#!/usr/bin/python
import gps
import time
import os

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            os.system('clear')
            print '          GPS Data'
            print '--------------------------------'
            print 'latitude    ' , getattr(report,'lat',0.0)
            print 'longitude   ' , getattr(report,'lon',0.0)
            print 'time utc    ' , getattr(report,'time','')
            print 'altitude    ' , getattr(report,'alt','nan')
            print 'epv         ' , getattr(report,'epv','nan')
            print 'ept         ' , getattr(report,'ept','nan')
            print 'speed       ' , getattr(report,'speed','nan')
            print 'climb       ' , getattr(report,'climb','nan')
            time.sleep(1)

    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
