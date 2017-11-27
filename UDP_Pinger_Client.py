import socket
import sys
import time

#Get the server hostname and port as command line arguments
argv = sys.argv
serverName = argv[1]
serverPort = int(argv[2])
#Create the Client Socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Set Timeout to one second
clientSocket.settimeout(1)
#initialize variables
sequence_number = 1
packetDrop = 0
RTTList=[]
#While loop to make 10 pings
while sequence_number < 11:
    startTime = time.clock()
    #Setup the message
    message = "Ping " + str(sequence_number) + " Start Time:" + str(startTime) + " "
    #Send message to server
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    #Try if it does not timeout
    try:
        #Recieve message back
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        RTT = (time.clock() - startTime)
        RTTList.append(RTT)
        #Printout the reply from
        print ("Reply from ", serverAddress, modifiedMessage.decode(),  "RTT: " + str(RTT))
        sequence_number += 1
        continue
    #If timeout, do this
    except socket.timeout:
        print("Request timed out")
        packetDrop += 1
        sequence_number += 1
        continue
#Get the average RTT
avgRTT = (sum(RTTList)/len(RTTList))
#Get the packet loss Percentage
packetLossPercentage = ((packetDrop/10)*100)
#Final print statement
print("The minimum RTT is: " + str(min(RTTList)) + "\nThe maximum RTT is: " + str(max(RTTList)) + "\nThe Average RTT is: " + str(avgRTT) + "\nThe packet loss is " , str(packetLossPercentage) + "%")
#Close the connection
clientSocket.close()
