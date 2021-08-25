from gevent import monkey; monkey.patch_all()
from gevent import sleep
 
from bottle import get, post, request, response, template
from bottle import GeventServer, run
import time
 
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
 
 
@get('/')
def index():
    #return sse_test_page
    return template('ssechart', deviceId="54ff6c066667515149512367", eventname="temperature", access_token="f177480fad1fcab0ef861d3d8e37ed4b37446e32")
 
 
@get('/stream')
def stream():
    # "Using server-sent events"
    # https://developer.mozilla.org/en-US/docs/Server-sent_events/Using_server-sent_events
    # "Stream updates with server-sent events"
    # http://www.html5rocks.com/en/tutorials/eventsource/basics/
 
    response.content_type  = 'text/event-stream'
    response.cache_control = 'no-cache'
 
    # Set client-side auto-reconnect timeout, ms.
    yield 'retry: 100\n\n'
 
    n = 1
 
    # Keep connection alive no more then... (s)
    end = time.time() + 60
    while time.time() < end:
        yield 'data: %i\n\n' % n
        n += 1
        sleep(1)
 
 
if __name__ == '__main__':
    run(host="192.168.0.30", port=8008, server=GeventServer)
