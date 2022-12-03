import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the host socket
mysock.connect(('data.pr4e.org',80))

# Access and retrieve the file from the host.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()