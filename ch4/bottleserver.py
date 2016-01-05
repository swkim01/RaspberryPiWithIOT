from bottle import route, run, template

@route('/')
@route('/<name>')
def index(name='World'):
    #return 'Hello %s!' % name
    return template('hello_template', name=name)

run(host='localhost', port=8080)
