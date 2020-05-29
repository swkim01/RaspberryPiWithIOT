from flask import Flask, render_template_string
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

sse_test_page = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8" />
		<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.min.js "></script>
		<script>
			$(document).ready(function() {
				var es = new EventSource("stream");
				es.onmessage = function (e) {
					$("#log").html($("#log").html()
						+ "<p>Event: " + e.event + ", data: " + e.data + "</p>");
				};
			})
		</script>
	</head>
	<body>
		<div id="log" style="font-family: courier; font-size: 0.75em;"></div>
	</body>
</html>
"""
 
 
@app.route('/')
def index():
    return render_template_string(sse_test_page)

@app.route('/send')
def send_message():
    sse.publish({"message": "hello!"}, type='greeting')
    return "Message sent!"

if __name__ == '__main__':
    app.run("localhost", 8000)
