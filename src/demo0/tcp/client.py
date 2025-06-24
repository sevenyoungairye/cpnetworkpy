from socket import * 

serverName = 'REMOTE SERVER IP'
serverName = '0.0.0.0'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM

clientSocket.connect((serverName, serverPort))

# TODO: upgreade loop send.
msg = input('please input msg(when u finished input, pelase type enter.):\n')
if (msg == 'exit'):
    clientSocket.close()
    print('end.')

clientSocket.send(msg.encode())
serverModifiedMsg = clientSocket.recv(2048)
print('from tcp server. ', serverModifiedMsg.decode())

