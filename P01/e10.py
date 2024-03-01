from Seq1 import Seq

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in genes:
    filename = "../sequences/" + gene + ".txt"
    s = Seq()
    s.read_fasta(filename)
    base_counts = s.count()
    most_frequent_base = max(base_counts, key=base_counts.get)
    print(f"Gene {gene}: Most frequent Base: {most_frequent_base}")