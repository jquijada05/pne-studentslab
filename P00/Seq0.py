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
        print("Gene", gene, "->  Length:", len(seq))

