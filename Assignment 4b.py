# Program Name: programB.py
# Course: IT3883/Section W01
# Student Name: Sidney Glover
# Assignment Number: Assignment 4
# Due Date: 04/01/2026
# Purpose: will listen for a string from program A. It will take the received string, convert it to all upper case, print the upper case string in Program B and send it back to Program A.

# Resources: socket module

import socket

HOST = '127.0.0.1'  #localhost
PORT = 50000       #port number
#Creates socket
socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binds
socket_connection.bind((HOST, PORT))
#Listening for connection
socket_connection.listen(1)
print("Waitng for connection ")
#New socket made
conn, addr = socket_connection.accept()
print("Connected by:", addr)
#Recieved 
data = conn.recv(1024)
#Makes into uppercase
answer = data.decode().upper()
#Prints as uppercase
print("Uppercase:", answer)
#Sent back to program a
conn.send(answer.encode())
#Closes
conn.close()
socket_connection.close()