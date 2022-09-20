

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

print(ord('a'))  #represents position for sorting
#ASCII - [1B] UTF-8 [1-4BYTE]  IF 1 UTF -8 IS ASCII COMP
#UTF-32 [4BYTE] UTF-16 [2BYTE]
    