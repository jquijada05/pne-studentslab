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

    def count(self):
        dna_count = {"A": 0, "C": 0, "G": 0, "T": 0}
        for nucleotide in self.strbases:
            if nucleotide in dna_count:
                if self.strbases == "NULL" or self.strbases == "ERROR!!":
                    dna_count[nucleotide] = 0
                else:
                    dna_count[nucleotide] += 1
        return dna_count

    def reverse(self):
        if self.strbases == "NULL":
            return "NULL"
        if self.strbases == "ERROR!!":
            return "ERROR"
        return self.strbases[::-1]

    def complement(self):
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement_seq = ""
        if self.strbases == "NULL":
            return "NULL"
        if self.strbases == "ERROR!!":
            return "ERROR"
        for base in self.strbases:
            complement_seq += complement_dict.get(base, base)
        return complement_seq

def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Sequence {i + 1}: (Length: {seq.len()}) {seq}")
        print(f"Bases: {seq.count()}")
        print(f"Rev: {seq.reverse()}")
        print(f"Com: {seq.complement()}")

seq_list = [Seq(""), Seq("ACTGA"), Seq("Invalid sequence")]
print_seqs(seq_list)