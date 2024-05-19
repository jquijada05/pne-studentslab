import http.server
import socketserver
import termcolor
from pathlib import Path
import json
from urllib.parse import parse_qs, urlparse, quote
import jinja2 as j
from Seq1 import Seq

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents
def get_json_object(object):
    Server = "rest.ensembl.org"
    Endpoint = object
    Params = "?content-type=application/json"

    conn = http.client.HTTPConnection(Server)

    try:
        conn.request("GET", Endpoint + Params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data = r1.read().decode("utf-8")
    json_object = json.loads(data)
    return json_object

def get_info(sequence):
    info = f"Total length: {sequence.len()}<br>"
    for base in ["A", "C", "G", "T"]:
        count = sequence.count_base(base)
        percentage = count / sequence.len() * 100 if sequence.len() > 0 else 0
        info += f"{base}: {count} ({percentage}%)<br>"
    return info
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        print(path, arguments)

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        if path == "/":
            contents = Path('index.html').read_text()
        elif path == "/listSpecies":
            person = get_json_object("/info/species")
            def get_limit_species(number):
                limit_species = ""
                for i in range(0, int(number)):
                    limit_species += "• " + person['species'][i]["display_name"] + "<br>"
                return limit_species
            if len(arguments) == 0:
                contents = read_html_file('limit.html').render(context={"total_length": len(person['species']),"species": get_limit_species(317)})
            else:
                contents = read_html_file('limit.html').render(context={"total_length": len(person['species']), "limit": arguments["limit"][0], "species": get_limit_species(arguments['limit'][0])})
        elif path == "/karyotype":
            try:
                person = get_json_object("/info/assembly/" + quote(arguments["species"][0].replace(" ", "%20")))
                def get_karyotype():
                    karyotype = ""
                    for i in person['karyotype']:
                        karyotype += i + "<br>"
                    return karyotype
                contents = read_html_file('karyotype.html').render(context={"karyotype": get_karyotype()})
            except KeyError:
                contents = Path('error.html').read_text()
        elif path == "/chromosomeLength":
            try:
                person = get_json_object("/info/assembly/" + arguments["species"][0])
                def get_chromosome_length():
                    for i in person["top_level_region"]:
                        if i["name"] == arguments["chromo"][0]:
                            length = i["length"]
                            return length
                contents = read_html_file('chromosome_length.html').render(context={"chromosome_length": get_chromosome_length()})
            except KeyError:
                contents = Path('error.html').read_text()
        elif path == "/geneSeq":
            try:
                person = get_json_object("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])
                gene_id = person.get("id")
                sequence = get_json_object("/sequence/id/" + gene_id)
                seq = sequence["seq"]
                contents = read_html_file('geneSeq.html').render(context={"gene": arguments["gene"][0], "seq": seq})
            except KeyError:
                contents = Path('error.html').read_text()
        elif path == "/geneInfo":
            try:
                person = get_json_object("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])
                gene_id = person.get("id")
                sequence = get_json_object("/sequence/id/" + gene_id)
                info = f"Start: {person['start']}" + "<br>"
                info += f"End: {person['end']}" + "<br>"
                info += f"Length: {len(sequence['seq'])}" + "<br>"
                info += f"ID: {person['id']}" + "<br>"
                info += f"Chromosome: {person['seq_region_name']}"
                contents = read_html_file('geneInfo.html').render(context={"gene": arguments["gene"][0], "info": info})
            except KeyError:
                contents = Path('error.html').read_text()
        elif path == "/geneCalc":
            try:
                person = get_json_object("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])
                gene_id = person.get("id")
                sequence = get_json_object("/sequence/id/" + gene_id)
                s = Seq(sequence["seq"])
                contents = read_html_file('geneCalc.html').render(context={"gene": arguments["gene"][0], "calc": get_info(s)})
            except KeyError:
                contents = Path('error.html').read_text()
        elif path == "/geneList":
            try:
                import requests
                url = "https://rest.ensembl.org/overlap/region/human/" + arguments["chromo"][0] + ":" + arguments["start"][0] + "-" + arguments["end"][0] + "?feature=gene;content-type=application/json"
                response = requests.get(url)
                json_data = response.json()
                print(json_data)
                genes = ""
                for i in json_data:
                    if "external_name" in i:
                        genes += i["external_name"]
                contents = read_html_file('geneList.html').render(context={"gene_list": genes})
            except KeyError:
                contents = Path('error.html').read_text()
        else:
            contents = Path('error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
