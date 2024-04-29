import http.client
import json
from Seq1 import Seq

genes = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": 'ENSG00000212379',
    "MIR633": 'ENSG00000207552',
    "TTTY4C": 'ENSG00000228296',
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

def get_info(sequence):
    info = f"Total length: {sequence.len()}\n"
    for base in ["A", "C", "G", "T"]:
        count = sequence.count_base(base)
        percentage = round(count / sequence.len() * 100 if sequence.len() > 0 else 0, 1)
        info += f"{base}: {count} ({percentage}%)\n"
    return info

gene = input("Write the gene name:")
if gene in genes:
    Server = "rest.ensembl.org"
    Endpoint = f"/sequence/id/{genes[gene]}"
    Params = "?content-type=application/json"
    URL = Server + Endpoint + Params

    print()
    print(f"Server: {Server}")
    print(f"URL: {URL}")

    conn = http.client.HTTPConnection(Server)

    try:
        conn.request("GET", Endpoint + Params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data = r1.read().decode("utf-8")
    person = json.loads(data)
    print(f"Gene: {gene}")
    print(f"Description: {person['desc']}")
    seq = person['seq']
    sequence = Seq(seq)
    print(get_info(sequence))
    base_counts = sequence.count()
    most_frequent_base = max(base_counts, key=base_counts.get)
    print(f"Most frequent Base: {most_frequent_base}")
else:
    print("The gene is not valid.")