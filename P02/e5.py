from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.95"
PORT = 8081
c = Client(IP, PORT)
print(c)
filename = "../sequences/FRAT1.txt"
s = Seq()
seq = s.read_fasta(filename)
