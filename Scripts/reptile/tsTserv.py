from socket import *
from time import ctime


HOST = ' '
PORT = 3154
BUFSIZ = 1024
ADDR= (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('Waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpSerSock.recv(BUFSIZ)
        if not data:
            break
        tcpSerSock.send('[%s]%s' % (bytes(ctime(), 'utf-8'),data))
        tcpCliSock.close()
    tcpSerSock.close()