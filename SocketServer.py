'''
Write a program that creates a simple echo server program that runs on
a host and port available at your development disposal.  Then write a
simple echo client program that runs on the same host and port as the
server you are using.  Use Python's socket module to establish socket
objects for both the client and server.  The server will first bind to
the HOST and PORT used for your solution then listen for a connection
request from the client. Have the server accept the client request.
The client will then send a message to the server.  The server will
receive the message and send an echo back to the client mirroring the
message received.
Close the network connection when either one of the parties closes
its connection or sends an empty string.


'''
import socket

HOST = socket.gethostname()
PORT = 50007 # arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))

except socket.error as e:
    print(e)

s.listen(5)
conn, addr = s.accept()

print ('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
conn.close()

