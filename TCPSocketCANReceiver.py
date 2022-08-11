import socket
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #Initialize port
    port = 23456
    data = []
    timeData = []
    dataPacketNum = []

    #Create socket
    s = socket.socket()
    host = socket.gethostname()

    #Bind to port
    s.bind((host, port))

    #Wait for sender to connect
    s.listen(5)
    print("Waiting for sender....")
    

    #Establish connection with sender
    c, addr = s.accept()
    print("Receiving data...")

    start_time = time.time()
    #Receive data
    for i in range(0, 350000):
        #Send a request to the sender
        reply = "CAN" 
        c.send(reply.encode("utf-8"))
        
        #Receive bytes
        data += c.recv(160)
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

    c.close() 