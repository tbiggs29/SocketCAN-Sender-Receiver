import socket
import os

if __name__ == '__main__':
    #Initialize port
    port = 23456

    #Get IP
    IP = socket.gethostbyname(socket.gethostname())
    
    # Create a UDP socket at client side
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    message = str.encode("Connected")
    client.sendto(message, (IP, port))

    
    for i in range(0, 350000):
        #Receive request from receiver
        request = client.recvfrom(1024) #Request recieved
        if(request[0].decode("utf-8") == "CAN"):
            #Send data
            content = os.urandom(160)
            client.sendto(content, (IP, port))

    client.close() 