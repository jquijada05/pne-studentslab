from Seq1 import Seq

# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.read_fasta("../sequences/U5.txt")

print(f"Sequence: (Length: {s.len()}) {s}")
print(f"Bases: {s.count()}")
print(f"Rev: {s.reverse()}")
print(f"Com: {s.complement()}")
