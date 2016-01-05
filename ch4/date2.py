#!/usr/bin/python

#import modules for CGI handling 
import  time

print "Content-type:text/xml\r\n\r\n"
print "<?xml version='1.0'?>"
print "<date>%s</date>" % time.ctime()
