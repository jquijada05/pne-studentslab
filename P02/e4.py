from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.95"
PORT = 8081
c = Client(IP, PORT)
print(c)
genes = ["U5", "FRAT1", "ADA"]
for gene in genes:
    filename = "../sequences/" + gene + ".txt"
    s = Seq()
    response = c.talk(f"Sending {gene} Gene to the server...")
    print(f"To server: Sending {gene} Gene to the server...")
    print(f"From server: {response}")
    response = c.talk(s.read_fasta(filename))
    print(f"To server: {s.read_fasta(filename)}")
    print(f"From server: {response}")
