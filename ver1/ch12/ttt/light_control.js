#!/usr/bin/env node

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0"
var http = require("http");
var util = require("util");
var url = require("url");
var WebSocket = require('ws');
var gpio = require("pi-gpio");
gpio.open(12, "output", function(err) { });

function sendTurnOn(ws) {
    var json = JSON.stringify({ path :'/api/v1/actor/perform/device/lighting',
                             requestID :'1',
                             perform :'on',
                             parameter :JSON.stringify({ brightness: 100,
                             color: { model: 'rgb', rgb: { r: 255, g: 255, b: 255 }}})
                            });
    ws.send(json);
    console.log( json );
}
function sendTurnOff(ws) {
    var json = JSON.stringify({ path :'/api/v1/actor/perform/device/lighting',
                             requestID :'2',
                             perform :'off',
                             parameter :''
                            });
    ws.send(json);
    console.log( json );
}

function toggleLight(cmd) {
    if (cmd == "1") {
        gpio.write(12, 1, function(err) { });
    } else if (cmd == "2") {
        gpio.write(12, 0, function(err) { });
    }
}
function onRequest(request, response) {
    var ws;
    console.log("Request recieved.");
    var pathname = url.parse(request.url).pathname;
    response.writeHead(200, {"Content-Type":"text/html"});

    ws = new WebSocket('ws://127.0.0.1:8887/manage');
    console.log("Created websocket.");

    ws.onopen = function(event) {
        console.log("Opened websocket to steward.");
        if ( pathname == "/on") {
            sendTurnOn(ws);
        } else if ( pathname == "/off") {
            sendTurnOff(ws);
        } else {
            response.write("<h2>Unrecognised request</h2>");
            ws.close();
            response.end();
        }
    };

    ws.onmessage = function(event) {
        //console.log("Socket message: " + util.inspect(event.data));
        response.write( "<h2>Turning lightbulb '" + pathname +"'</h2>");
        ws.close();
        response.end();
        var info = JSON.parse(event.data);
        toggleLight(info["requestID"]);
    };

    ws.onclose = function(event) {
        console.log("Socket closed: " + util.inspect(event.wasClean));
        //gpio.close(12);
    };

    ws.onerror = function(event) {
        console.log("Socket error: " + util.inspect(event, {depth: null}));
        try {
            ws.close();
            console.log("Closed websocket.");
        } catch (ex) {}
    };
}
var server = http.createServer(onRequest).listen(9999);
console.log("Server started on port 9999.");

var MIN = 22;
var MAX = 27;

setInterval( function() {
    var ws;
    console.log("Test started.");
    ws = new WebSocket('ws://127.0.0.1:8887/manage');
    console.log("Created websocket.");
    var dev = "/device/climate/arduino/meteo";
    ws.onopen = function(event) {
        console.log("Opened websocket to steward.");
        var json = JSON.stringify({ path:'/api/v1/actor/list'+dev,
                                        requestID :'1',
                                        options :{ depth: 'all' } });
        ws.send(json);
    };

    ws.onmessage = function(event) {
        //console.log("Socket message: " + util.inspect(event.data));
        var info = JSON.parse(event.data);
        var result = info["result"];
        if (result != null) {
            var devinfo = result[dev];
            if (devinfo != null) {
                var firstdev = devinfo["device/1"];
                var temp = firstdev["info"]["temperature"];
                var humi = firstdev["info"]["humidity"];
                console.log("Temperature: " + temp + ", Humidity: " + humi);
                if ( Number(temp) < MIN) {
                    console.log("Turn on light by temperature");
                    sendTurnOn(ws);
                } else if (Number(temp) > MAX) {
                    console.log("Turn off light by temperature");
                    sendTurnOff(ws);
                }
            } else {
                ws.close();
            }
        } else {
            toggleLight(info["requestID"]);
            ws.close();
        }
    };

    ws.onclose = function(event) {
        console.log("Socket closed: " + util.inspect(event.wasClean));
        //gpio.close(12);
    };

    ws.onerror = function(event) {
        console.log("Socket error: " + util.inspect(event, {depth: null}));
        try {
            ws.close();
            console.log("Closed websocket.");
        } catch (ex) {}
    };
}, 10000);
