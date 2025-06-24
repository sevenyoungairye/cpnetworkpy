from socket import * 

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
msg = input('please input msg(when u finished input, pelase type enter.):\n')
clientSocket.sendto(msg.encode(), (serverName, serverPort))
serverModifiedMsg, serverAddr = clientSocket.recvfrom(2048)
print(serverModifiedMsg.decode())
clientSocket.close()
