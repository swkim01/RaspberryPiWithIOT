from flask import Flask, request, url_for, redirect, session, escape

app = Flask(__name__)
app.secret_key = 'A1Zr51j/3yX R~X@H!jmN]kAX/,?UT'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

def check_login(username, password):
    if username=="pi" and password=="raspberry":
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'])
def do_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if check_login(username, password):
            session['username'] = username
        return redirect(url_for('index'))
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.route('/logout', methods=['GET'])
def do_logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__' :
    app.run(host='localhost', port=8080)
