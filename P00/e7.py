from pathlib import Path
file_contents = Path("../sequences/U5.txt").read_text()
first_line_i = file_contents.find("\n")
seq_dna = file_contents[first_line_i:]
seq = seq_dna.replace("\n", "")
from Seq0 import *
seq_complement(seq)
print("Gene U5:")
print("Frag:", seq[0: 21])
complement_fragment = seq_complement(seq[0: 21])
print("Comp:", complement_fragment)
