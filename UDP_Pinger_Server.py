import random
import socket
import sys


#Get the server hostname and port as command line arguments
argv = sys.argv
host = argv[1]
serverPort = int(argv[2])

#Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Assign IP address and port number to socket
serverSocket.bind((host, serverPort))

while 1:
    #Generate random number in the range of 0 to 10
    randNum = random.randint(0,10)
    #recieve the client packet along with the address it is coming from
    message, clientAddress = serverSocket.recvfrom(1024)
    #If random number is less is than 4, we consider the packet lost and do not respond
    if randNum < 4:
        continue
    #Send the message back
    serverSocket.sendto(message, clientAddress)
 
