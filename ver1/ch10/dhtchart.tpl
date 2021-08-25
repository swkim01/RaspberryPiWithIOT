<!DOCTYPE HTML>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>실시간 온도, 습도 측정기</title>
  <link rel="stylesheet" href="//code.jquery.com/mobile/1.4.3/jquery.mobile-1.4.3.min.css" />
  <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
  <script src="//code.jquery.com/mobile/1.4.3/jquery.mobile-1.4.3.min.js"></script>
  <script src="//cdnjs.cloudflare.com/ajax/libs/highcharts/4.0.4/highcharts.js"></script>

<script>
    var chart;  // 온도
    var chart2;  // 습도
    var pollUri="/events";

    function pollEvent() {
        $.getJSON(pollUri,
            function(data) {
                var t = new Date();
                t.setHours(t.getHours() + 9);
                chartAddPoint([t.getTime(), Number(data.temperature)]);
                chart2AddPoint([t.getTime(), Number(data.humidity)]);
            }
        );
        setTimeout('pollEvent()', 5000);
    }

    pollEvent();
    
    function chartAddPoint(tval) {
        var series = chart.series[0],
        shift = series.data.length > 20;
        chart.series[0].addPoint(eval(tval), true, shift);
    }

    function chart2AddPoint(hval) {
        var series2 = chart2.series[0],
        shift2 = series2.data.length > 20;
        chart2.series[0].addPoint(eval(hval), true, shift2);
    }

    $(function() {
        // 온도
        chart = new Highcharts.Chart({
            chart: {
                renderTo: 'temp',
                defaultSeriesType: 'spline',
            },
            title: {
                text: '실시간 온도 데이터'
            },
            xAxis: {
                type: 'datetime',
                tickPixelInterval: 120,
                maxZoom: 20 * 1000
            },
            yAxis: {
                minPadding: 0.2,
                maxPadding: 0.2,
                title: {
                    text: '온도 ( °C )',
                    margin: 20
                }
            },
            series: [{
                name: '온도',
                data: []
            }]
        });
        // 습도
        chart2 = new Highcharts.Chart({
            chart: {
                renderTo: 'humi',
                defaultSeriesType: 'spline',
            },
            title: {
                text: '실시간 습도 데이터'
            },
            xAxis: {
                type: 'datetime',
                tickPixelInterval: 120,
                maxZoom: 20 * 1000
            },
            yAxis: {
                minPadding: 0.2,
                maxPadding: 0.2,
                title: {
                    text: '습도 ( % )',
                    margin: 20
                }
            },
            series: [{
                name: '습도',
                data: []
            }]
        });
    });
</script>
</head>
<body>
  <div id="temp" style="width: 100%; height: 300px; margin-left:-5px;"></div>
  <div id="humi" style="width: 100%; height: 300px; margin-left:-5px;"></div>
</body>
</html>
