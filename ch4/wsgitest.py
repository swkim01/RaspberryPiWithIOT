#!/usr/bin/env python

def application(environ, start_response):
    status = '200 OK'
    output = '<H2>Hello WSGI!</H2>'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8008, application)
    server.serve_forever()
