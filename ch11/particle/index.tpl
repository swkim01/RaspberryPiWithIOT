<html>
<head>
<script>
  var deviceId = "{{device_id}}";
  var accessToken = "{{access_token}}";
  var ledUri = "https://api.spark.io/v1/devices/"+deviceId+"/led";
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
    var send ="access_token="+accessToken+"&params=" + (value != 0 ? "HIGH":"LOW");
    request.open('POST', ledUri, true);
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.send(send);
  }

  function sseChart() {
     window.location.href='/ssechart';
  }
</script>
</head>
<body>
<h1>스파크 제어</h1>
<h2>LED 제어</h2>
<input type='button' onClick="ledControl()" value="ON/OFF" />
<h2>온도/습도 모니터링</h2>
<input type='button' onClick="sseChart()" value="모니터링" />
</body>
</html>
