from flask import Flask, request, url_for, Response, redirect, abort

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/object/<int:id>')
def callback(id):
    assert isinstance(id, int)
    return url_for('callback', id=id)

@app.route('/login', methods=['GET'])
def show_loginform():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

def check_login(username, password):
    if username=="pi" and password=="raspberry":
        return True
    else:
        return False

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@app.route('/question', methods=['GET'])
def question():
    return request.args.get('answer')

@app.route('/question', methods=['POST'])
def form_question():
    return request.form.get('answer')

@app.route('/json', methods=['POST'])
def json():
    print(request.get_json())
    return str(request.get_json())

@app.route('/path', methods=['GET', 'POST'])
def get_path():
    return ("path: %s<br>"
            "script_root: %s<br>"
            "url: %s<br>"
            "base_url: %s<br>"
            "url_root: %s<br>") % (request.path, request.script_root,
                    request.url, request.base_url, request.url_root)

@app.route('/response')
def custom_response():
    resp = Response("response test")
    resp.headers.add('Text-Name', 'Response Test')
    resp.set_data('This is a response test')
    return resp

@app.route('/hi')
def hi():
    #return redirect(url_for("hello_world"))
    return redirect("/hello")

@app.errorhandler(404)
def error404(error):
    return "This pag is not existed."

@app.route('/wrong')
def wrong():
    abort(401, "Sorry. That page is not existed.")

