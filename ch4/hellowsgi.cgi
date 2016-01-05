#!/usr/bin/env python

def application(environ, start_response):
    status = '200 OK'
    output = '<H2>Hello World!</H2>'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

from wsgiref.handlers import CGIHandler
CGIHandler().run(application)
