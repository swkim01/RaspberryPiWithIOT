#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
login_id = form.getvalue('loginid')
password  = form.getvalue('password')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Login CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s</h2>" % (login_id)
print "</body>"
print "</html>"
