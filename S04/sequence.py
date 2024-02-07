from pathlib import Path
FILENAME = "ADA.txt"
file_contents = Path(FILENAME).read_text()
index = file_contents.find("\n")
file_contents = file_contents[index:].replace("\n", "")
print(len(file_contents))

