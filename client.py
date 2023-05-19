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

HOST = "127.0.0.1"
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))                                 # Connect to the server

while True:                   # Receive quiz questions from the server and send the answers
    question = client_socket.recv(1024).decode()
    if not question:
        break
    print(question)

    # comment out the code below to just get the questions printed
    answer = input()
    client_socket.sendall(answer.encode())                          # send entered answer
    result = client_socket.recv(1024).decode()                      # receive "correct" or "incorrect" message
    print(result)

client_socket.close()
