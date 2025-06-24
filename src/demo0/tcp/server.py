from socket import * 
sp = 12000
ss = socket(AF_INET, SOCK_STREAM) # note
ss.bind(('0.0.0.0', sp))
ss.listen(1)
print('the server is ready to receive')
while True: 
    connectionSocket, addr = ss.accept()
    sentence = connectionSocket.recv(1024).decode()
    print('get msg from client: ', sentence)
    capitalizedSetence = sentence.upper()
    connectionSocket.send(capitalizedSetence.encode())
    connectionSocket.close()
