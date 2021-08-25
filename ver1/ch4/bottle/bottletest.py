from bottle import route, run, request, response, static_file, error, abort, get, post

@route('/')
@route('/hello')
#def hello_world():
#    return 'Hello World!'
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)
@route('/show/<name:re:[a-z]+')
def callback(name):
    assert name.isalpha()
@route('/static/<filename:re:.*.png>')
def static(filename):
    return static_file(filename, root='/home/pi/python_games/')

@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

def check_login(username, password):
    if username=="aaa" and password=="pass":
        return True
    else:
        return False

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@error(404)
def error404(error):
    return "That page is not existed"

@route('/wrong')
def wrong():
    abort(401, 'Sorry. Access denied.')

run(host='localhost', port=8008)
