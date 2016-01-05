<html>
<head>
<script>
  var ledUri = "/led";
  var value = 0;
  function ledControl() {
    if ( window.XMLHttpRequest ) {
      request = new XMLHttpRequest();
    }
    if ( !request ) {
      alert("XMLHttpRequest Error");
      return false;
    }
    value = !value;
    var send =(value != 0 ? "ON":"OFF");
    request.open('POST', ledUri, true);
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.send(send);
  }

  function dhtChart() {
     window.location.href='/dhtchart';
  }
</script>
</head>
<body>
<h1>ESP8266/NODEMCU 제어</h1>
<h2>LED 제어</h2>
<input type='button' onClick="ledControl()" value="ON/OFF" />
<h2>온도/습도 모니터링</h2>
<input type='button' onClick="dhtChart()" value="모니터링" />
</body>
</html>
