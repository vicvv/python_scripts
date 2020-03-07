

import socket

# echo client program
HOST = socket.gethostname()
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
    s.send(b'Hello, Foothill!')
    data = s.recv(1024)
except socket.error as e:
    print(e)


s.close()
print('Received', repr(data))
