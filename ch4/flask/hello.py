from flask import Flask, request, url_for, Response, make_response, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/object/<int:id>')
def callback(id):
    assert isinstance(id, int)
    return url_for('callback', id=id)

with app.test_request_context():
    print(url_for('callback', id=1))

#@app.route('/question', methods=['GET'])
#def question():
#    return request.args.get('answer')

#@app.route('/question', methods=['POST'])
#def form_question():
#    return request.form.get('answer')

@app.route('/question', methods=['GET', 'POST'])
def question():
    return request.values.get('answer')

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

#@app.route('/response')
#def custom_response():
#    resp = Response("응답 테스트")
#    resp.headers.add('Text-Name', 'Response Test')
#    resp.set_data('이것은 응답 텍스트입니다')
#    return resp

@app.route('/response')
def custom_response():
    resp = make_response('이것은 응답 텍스트입니다')
    resp.headers.add('Text-Name', 'Response Test')
    return resp

@app.route('/cookie')
def hello_again():
    if request.cookies.get("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response = make_response("Hello there! Nice to meet you")
        response.set_cookie("visited", "yes")
        return response

@app.route('/test')
def test():
    return render_template("test.html", person="Kim", friends=["Lee", "Park"])

@app.route('/base')
def base():
    return render_template("base.html")

@app.route('/child')
def child():
    return render_template("child.html", items=[0, 1, 2, 3])

if __name__ == '__main__' :
    #app.run(host='localhost', port=5000)
    app.run()
