#Practice 0
#E1
def seq_ping():
    print("OK")
#E2
def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    first_line_i = file_contents.find("\n")
    seq_dna = file_contents[first_line_i:]
    print("The first 20 bases are: ", seq_dna[0: 21])
#E3
def seq_len(seq):
    return len(seq)
#E4
def seq_count_base(seq, base):
    base_count = seq.count(base)
    return base_count
#E5
def seq_count(seq):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for i in seq:
        if i in bases:
            bases[i] += 1
    return bases
#E6
def seq_reverse(seq, number):
    print("Fragment:", seq[0:number])
    print("Reverse:", seq[:number][::-1])
#E7
def seq_complement(seq):
    complement_seq = ""
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    for i in seq:
        complement_seq += complement[i]
    return complement_seq
#E8
def most_frequent_base(seq):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for i in seq:
        if i in bases:
            bases[i] += 1
    return max(bases, key=bases.get)

