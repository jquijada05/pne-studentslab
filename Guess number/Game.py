import random
import socket
PORT = 8081
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((IP, PORT))
ls.listen()
print("SEQ Server configured!")
try:
    while True:
        print("Waiting for clients...")
        (rs, address) = ls.accept()
        msg = rs.recv(2048).decode("utf-8")
        send_bytes = str.encode(response)
        rs.send(send_bytes)
        rs.close()
except socket.error:
    print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))
except KeyboardInterrupt:
    print("Server stopped by the user")

ls.close()

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []
    def guess(self, number):
        self.attempts.append(number)
        if number == self.secret_number:
            response = f"You won after {len(self.attempts)} attempts"
        elif number < self.secret_number:
            response = "Lower"
        elif number > self.secret_number:
            response = "Higher"

