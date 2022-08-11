from email.errors import MultipartInvariantViolationDefect
from re import M
import socket
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #Initialize port
    port = 23456
    data = []
    timeData = []
    dataPacketNum = []
    
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip    
    UDPServerSocket.bind((socket.gethostname(), port))
    print("Waiting for sender...")
    bytesAddressPair = UDPServerSocket.recvfrom(1024)
    message = bytesAddressPair[0].decode("utf-8")
    address = bytesAddressPair[1]
    print("Receiving data...")

    start_time = time.time()
    #Receive data
    for i in range(0, 350000):
        #Send a request to the sender
        reply = "CAN" 
        UDPServerSocket.sendto(reply.encode(), address)
        
        #Receive bytes
        data, addr = UDPServerSocket.recvfrom(160) 
        timeData.append((time.time() - start_time)*1000)
        start_time = time.time()
        dataPacketNum.append(i/1000)
        
    print("Plotting...")

    #Plot time difference
    plt.figure(figsize=(8, 7))
    plt.subplot(1, 2, 1)
    plt.scatter(dataPacketNum, timeData)
    plt.xlabel('TCP Socket Data Packet Number (in thousands)')
    plt.ylabel('Delta time (in ms): Received CAN bytes over TCP Socket Data Packets')

    plt.subplot(1, 2, 2)
    plt.boxplot(timeData)
    plt.show()

    UDPServerSocket.close()