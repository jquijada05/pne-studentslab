from Seq1 import Seq
def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Sequence {i + 1}: (Length: {seq.len()}) {seq}")
        print(f"Bases: {seq.count()}")
        print(f"Rev: {seq.reverse()}")
        print(f"Com: {seq.complement()}")

seq_list = [Seq(""), Seq("ACTGA"), Seq("Invalid sequence")]
print_seqs(seq_list)