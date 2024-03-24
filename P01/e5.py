class Seq:

    def __init__(self, strbases=None):
        if strbases == "":
            print("NULL sequence created")
            self.strbases = "NULL"
            return
        bases = ["A", "C", "G", "T"]
        for i in strbases:
            if i not in bases:
                self.strbases = "ERROR!!"
                print("ERROR!!")
                return
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR!!":
            return 0
        return len(self.strbases)

def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Sequence {i + 1}: (Length: {seq.len()}) {seq}")

seq_list = [Seq(""), Seq("ACTGA"), Seq("Invalid sequence")]
print_seqs(seq_list)
from Seq1 import Seq

def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Sequence {i + 1}: (Length: {seq.len()}) {seq}")
        for base in ["A", "C", "G", "T"]:
            count = seq.count_base(base)
            print(f"{base}: {count}")

seq_list = [Seq(""), Seq("ACTGA"), Seq("Invalid sequence")]
print_seqs(seq_list)
