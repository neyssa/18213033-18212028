import socket

HOST = '192.168.1.110'    #server name goes in here
PORT = 11111
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))

msg = raw_input('Enter your name: ')
while(1):
    print 'Hello! Welcome to my page. What kind of files do you want?'
    print 'Click "1" to download hello.txt '
    print 'Click "2" to download def.txt '

    x = raw_input('Enter your choice: ')

    if x == "1":
        with open('abc.txt', 'rb') as file_to_send:
            for data in file_to_send:
                socket.sendall(data)
        print 'end'

    elif x == "2":
        with open('def.txt', 'rb') as file_to_send:
            for data in file_to_send:
                socket.sendall(data)
        print 'end'
socket.close()
