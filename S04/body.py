from pathlib import Path
FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
first_line_i = file_contents.find("\n")
seq_dna = file_contents[first_line_i:]
print(seq_dna)

list_contents = file_contents.split("\n")
for i in range(1, len(list_contents)):
    print(list_contents[i])