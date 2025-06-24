from socket import * 

severPort = 12000
serverHost = '0.0.0.0'
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverHost, severPort))

print('the server is ready to receive.')

while True:
    msg, clientAddr = serverSocket.recvfrom(2048)
    modifyMsg = msg.decode().upper()
    print('get msg from client. ', modifyMsg, clientAddr)
    serverSocket.sendto(modifyMsg.encode(), clientAddr)