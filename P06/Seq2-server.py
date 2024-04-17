import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import Seq
# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

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
            contents = Path('html/index.html').read_text()
        elif path == "/ping":
            contents = read_html_file('ping.html').render(context={"todisplay": arguments})
        elif path == "/get":
            sequences = ["TCAGTCAA", "CGATACGA", "CCAGTGCA", "TTTCAGTA", "CATGCTAG"]
            n = sequences[int(arguments["n"][0])]
            contents = read_html_file('get.html').render(context={"todisplay": arguments["n"][0], "sequence": n})
        elif path == "/gene":
            genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
            final_seq = ""
            gene = arguments.get("gene")[0]
            for i in range(0, 5):
                if gene == genes[i]:
                    filename = "../sequences/" + gene + ".txt"
                    sequence = Path(filename).read_text()
                    s = sequence.split("\n")[1:]
                    for i in s:
                        final_seq += i
                    contents = read_html_file('gene.html').render(context={"todisplay": arguments["gene"][0], "sequence": final_seq})
        elif path == "/operation":
            sequence = Seq(arguments["sequence"][0])
            if arguments["operation"][0] == "Info":
                result = get_info(sequence)
                contents = read_html_file('operation.html').render(context={"todisplay": sequence, "operation": arguments["operation"][0], "result": result})
            elif arguments["operation"][0] == "Comp":
                result = sequence.complement()
                contents = read_html_file('operation.html').render(context={"todisplay": sequence, "operation": arguments["operation"][0], "result": result})
            elif arguments["operation"][0] == "Rev":
                result = sequence.reverse()
                contents = read_html_file('operation.html').render(context={"todisplay": sequence, "operation": arguments["operation"][0], "result": result})
        else:
            contents = Path('html/error.html').read_text()

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
