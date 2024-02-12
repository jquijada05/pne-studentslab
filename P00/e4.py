from pathlib import Path
bases = ["A", "C", "G", "T"]
genes = ["U5", "ADA", "FRAT1", "FXN"]
for gene in genes:
    filename = "../sequences/" + gene + ".txt"
    file_contents = Path(filename).read_text()
    first_line_i = file_contents.find("\n")
    seq_dna = file_contents[first_line_i:]
    seq = seq_dna.replace("\n", "")
    print(f"\nGene {gene}:")
    for base in bases:
        from Seq0 import *
        count = seq_count_base(seq, base)
        print(f"  {base}: {count}")
