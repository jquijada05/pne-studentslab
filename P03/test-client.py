from Client0 import Client
PRACTICE = 3
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)
print(c)
print("* Testing PING...")
get_ping = c.talk("PING")
print(get_ping)

print("\n* Testing GET...")
for i in range(0, 4):
    get_response = c.talk("GET " + str(i))
    print(f"GET {i}: {get_response}")

sequence = c.talk("GET 0")

print("\n* Testing INFO...")
info_response = c.talk(f"INFO {sequence}")
print(info_response)

print("\n* Testing COMP...")
comp_response = c.talk(f"COMP {sequence}")
print(f"COMP {sequence}")
print(comp_response)

print("\n* Testing REV...")
rev_response = c.talk(f"REV {sequence}")
print(f"REV {sequence}")
print(rev_response)

print("\n* Testing GENE...")
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in genes:
    gene_response = c.talk(f"GENE {gene}")
    print(f"GENE {gene}")
    print(gene_response)