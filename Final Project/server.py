import http.server
import socketserver
import termcolor
from pathlib import Path
import json
from urllib.parse import parse_qs, urlparse
import jinja2 as j
# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents
def get_json_data(path):
    Server = "rest.ensembl.org"
    Endpoint = "/info" + path
    Params = "?content-type=application/json"
    URL = Server + Endpoint + Params

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
    return person

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
        elif path == "/limit":
            contents = Path('limit.html')
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
