import socket
import os

if __name__ == '__main__':
    #Initialize port
    port = 23456

    #Get IP
    IP = socket.gethostbyname(socket.gethostname())
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to receiver
    client.connect((IP, port))
    
    for i in range(0, 350000):
        #Receive request from receiver
        request = client.recv(1024).decode("utf-8") #Request recieved
        if(request == "CAN"):
            #Send data
            content = os.urandom(160)
            client.send(content)

    client.close() 