# Name: Nicholas Pizarro
# OSU Email: pizarron@oregonstate.edu
# Course: CS361 - SOFTWARE ENGINEERING 1
# Assignment 8: Microservice Implementation (Milestone #2)
# Due Date: 05/08/22

# citation:
# Computer Networking: A Top-Down Approach 8th Edition by James Kurose, Keith Ross (CHAPTERS 2.7)
# https://www.internalpointers.com/post/making-http-requests-sockets-python
# https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
# https://realpython.com/python-sockets/
# https://realpython.com/python-sockets/
# https://learn.microsoft.com/en-us/dotnet/fundamentals/networking/sockets/socket-services
# https://pythonprogramming.net/sockets-tutorial-python-3/#:~:text=recv(1024),1024%20bytes%20at%20a%20time.
# https://www.ibm.com/docs/en/i/7.2?topic=programming-how-sockets-work

import socket
import json

HOST = "127.0.0.1"
PORT = 65432

print("The server is running...")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()


with open('questions.json', 'r') as f:              # Load the quiz questions from a JSON file
    quiz_questions = json.load(f)

while True:                                         # Accept a new connection

    client_socket, client_address = server_socket.accept()

    for questions in range(len(quiz_questions)):    # Send the quiz questions to the client
        client_socket.sendall(quiz_questions[questions]['question'].encode())
        # comment out the code below to just get the questions printed

        client_response = client_socket.recv(1024).decode()

        if client_response.lower() == quiz_questions[questions]['answer'].lower():  # check if answer is correct
            client_socket.sendall("Correct!".encode())
        else:
            client_socket.sendall("Incorrect!".encode())

    client_socket.close()
