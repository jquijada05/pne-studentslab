with open("DNA.txt", "r") as f:
    dna_count = {"A": 0, "C": 0, "G": 0, "T": 0}
    for line in f:
        for nucleotide in line:
            if nucleotide in dna_count:
                dna_count[nucleotide] += 1

print(dna_count)