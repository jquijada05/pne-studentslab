from Seq1 import Seq
def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Sequence {i + 1}: (Length: {seq.len()}) {seq}")

seq_list = [Seq("ACTGA")]
print_seqs(seq_list)