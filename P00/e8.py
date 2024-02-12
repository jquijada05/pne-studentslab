genes = ["U5", "ADA", "FRAT1", "FXN"]
for gene in genes:
    from pathlib import Path
    filename = "../sequences/" + gene + ".txt"
    file_contents = Path(filename).read_text()
    first_line_i = file_contents.find("\n")
    seq_dna = file_contents[first_line_i:]
    seq = seq_dna.replace("\n", "")
    from Seq0 import *
    most_frequent_base(seq)
    most_freq_base = most_frequent_base(seq)
    print(f"Gene {gene}: Most frequent Base: {most_freq_base}")
