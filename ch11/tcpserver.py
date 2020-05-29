import socket

#HOST, PORT = "<서버 IP>", <포트>
HOST, PORT = "192.168.1.109", 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    print("Received: ", data)
conn.close()
