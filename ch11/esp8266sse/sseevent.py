from flask import Flask, Response, render_template_string
import time

app = Flask(__name__)
 
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
						+ "<p>Event: " + e.type + ", data: " + e.data + "</p>");
				};
                                es.addEventListener("temp", function(e) {
				    $("#log").html($("#log").html()
					+ "<p>Event: " + e.type + ", data: " + e.data + "</p>");
                                }, false);
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
    #return render_template('ssechart.html', deviceId="54ff6c066667515149512367", eventname="temperature", access_token="f177480fad1fcab0ef861d3d8e37ed4b37446e32")

n = 0
 
def get_message():
    '''this could be any function that block'''
    global n
    n += 1
    time.sleep(1)
    return n
 
@app.route('/stream')
def stream():
    # "Using server-sent events"
    # https://developer.mozilla.org/en-US/docs/Server-sent_events/Using_server-sent_events
    # "Stream updates with server-sent events"
    # http://www.html5rocks.com/en/tutorials/eventsource/basics/
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            #yield 'event: message\ndata: {}\n\n'.format(get_message())
            yield 'data: {}\n\nevent: temp\ndata: 1\n\n'.format(get_message())
            #yield 'data: {}\n\nevent: aaa\ndata: kkk\n\n'.format(get_message())
            #yield 'data: {}\n\n'.format(get_message())
    return Response(eventStream(), mimetype="text/event-stream")
 
if __name__ == '__main__':
    app.run(host="192.168.1.109", port=8008)
