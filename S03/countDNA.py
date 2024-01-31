seq_dna = input("Enter a DNA sequence: ")
dna_count = {"A": 0, "C": 0, "G": 0, "T": 0}
for nucleotide in seq_dna:
    if nucleotide in dna_count:
        dna_count[nucleotide] += 1

print("Total length: ", len(seq_dna))
print(dna_count)