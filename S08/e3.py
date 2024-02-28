import socket
# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.96" # depends on the computer the server is running

while True:
    question = input("Enter a message: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(question.encode())
    s.close()

