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
    count = seq.count(base)
    return count
#E5
def seq_count(seq):
    dna_count = {"A": 0, "C": 0, "G": 0, "T": 0}
    for line in seq:
        for nucleotide in line:
            if nucleotide in dna_count:
                dna_count[nucleotide] += 1
    return dna_count
#E6
def seq_reverse(seq, n):
    print("Fragment:", seq[0:n])
    print("Reverse:", seq[:n][::-1])
#E7
def seq_complement(seq):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement_seq = ""
    for base in seq:
        complement_seq += complement_dict.get(base, base)
    return complement_seq
#E8
def most_frequent_base(seq):
    base_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in seq:
        if base in base_count:
            base_count[base] += 1
    most_frequent = max(base_count, key=base_count.get)
    return most_frequent






