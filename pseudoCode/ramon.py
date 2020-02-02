# CST 311
# Programming Assignment 2
# Team 7
# Amir-Andy Alameddine
# Michael Lee
# Ramon Lucindo
# Sergio Quiroz

# UDPPingerClient.py

#Import socket module and import all of its contents
from socket import *
#Holds the name of the server's host name
serverName = 'localhost'
#Specify the Server Port Number
serverPort = 12000

#Create client socket.  AF_INET: underlying network is using IPv4
#SOCK_DGRAM: UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#Gets the user's input and stores into message
message = input('Input lowercase sentence:')
#Encodes the message into bytes and sends the message through the socket
#It also sends it to the server by specifying the server's hostname and port
#number to send it to
clientSocket.sendto(message.encode(),(serverName, serverPort))
#Gets the modified message from server (received from port 1024)
modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
#Decodes message and prints it
print(modifiedMessage.decode())
#Closes the socket after the message is received
clientSocket.close()
