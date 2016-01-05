import socket

HOST, PORT = "<서버 IP>", <포트>

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print "Received: ", data
