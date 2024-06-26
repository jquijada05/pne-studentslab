from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.103"
PORT = 8081
c = Client(IP, PORT)
print(c)
filename = "../sequences/FRAT1.txt"
s = Seq()
seq = s.read_fasta(filename)
fragments = []
for i in range(0, len(seq) + 1):
    fragment = seq[i:i+10]
    fragments.append(fragment)

for i in fragments[0:5]:
    msg = f"Fragment {fragments.index(i) + 1}: {i}"
    print(msg)
    print(c.talk(msg))