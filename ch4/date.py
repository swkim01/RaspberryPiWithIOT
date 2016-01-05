#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, time, datetime
cgitb.enable()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Date CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Date: %s</h2>" % time.ctime()
time_format = "%a, %d %b %Y %H:%M:%S %Z"
print "<h2>Date: %s</h2>" % (datetime.datetime.now().strftime(time_format))
print "</body>"
print "</html>"
