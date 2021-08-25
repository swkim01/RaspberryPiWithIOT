import sys, re
import socket, fcntl, struct
import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        print "Someone connected from {} : {}!".format(self.client_address[0], self.client_address[1])
        while True:
            d = raw_input('>> ')
            if re.compile('^[0-7][lh]$', re.I).match(d):
                self.request.send(d.lower())
            elif 'x' == d:
                self.request.close()
                self.server.shutdown()
                break
            else:
                print "Commands: 0h  Set pin D0 high"
                print "      	7l  Set pin D7 low"
                print "          	Any pin 0-7 may be set high or low"
                print "      	x   Exit"

def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADD
            struct.pack('256s', ifname[:15])
        )[20:24])

if __name__ == "__main__":
    ip,port = socket.gethostbyname(socket.gethostname()), 9000
    if ip.startswith("127."):
        interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wlan7","wifi0","ath0","ath1","ppp0"]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                #break
            except IOError:
                pass
    print "OK I'm listening on port {} here at IP address {}!".format(str(port),ip)
    print "Now run the following curl command in another window,"
    print "replacing <DEVICE_ID> and <ACCESS_TOKEN>."
    print "curl https://api.spark.io/v1/devices/<DEVICE_ID>/connect -d access_token=<ACCESS_TOKEN> -d ip={}".format(ip)

    # Create the server, binding to localhost on port 9000
    server = SocketServer.ThreadingTCPServer((ip, port), MyTCPHandler)

    # Activate the server
    server.serve_forever()
