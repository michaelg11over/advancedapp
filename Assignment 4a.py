# Program Name: programA.py
# Course: IT3883/Section W01
# Student Name: Sidney Glover
# Assignment Number: Assignment 4
# Due Date: 04/01/2026
# Purpose:  prompt the user to type in a string then transmit that string over a socket to program B
# Resources: socket module

import socket  

HOST = '127.0.0.1'  #localhost
PORT = 50000       #port number

#creates the socket
socket_connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connects to program b
socket_connection.connect((HOST, PORT))
#asks user for message to enter
user_input = input("Enter message: ")
#sends
socket_connection.send(user_input.encode())
#waiting
answer = socket_connection.recv(1024)
#decodes
print("Progam B answer: ", answer.decode())

socket_connection.close()