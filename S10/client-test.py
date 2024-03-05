from Client0 import Client
IP = "212.128.255.95"
PORT = 8081
c = Client(IP, PORT)
print(f"To server: {msg}")
print(f"From server: {c.talk(new_msg)}")
