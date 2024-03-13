from Client0 import Client
from Seq1 import Seq
PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.103"
PORT = 8081
PORT2 = 8080
c_odd = Client(IP, PORT)
c_even = Client(IP, PORT2)
print(c_odd)
print(c_even)
filename = "../sequences/FRAT1.txt"
s = Seq()
seq = s.read_fasta(filename)
fragments = []
for i in range(0, len(seq) + 1):
    fragment = seq[i:i+10]
    fragments.append(fragment)

for i in fragments[0:10]:
    msg = f"Fragment {fragments.index(i) + 1}: {i}"
    if fragments.index(i) % 2 == 0:
        print(msg)
        print(c_even.talk(msg))
    else:
        print(msg)
        print(c_odd.talk(msg))