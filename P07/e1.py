import http.client
import json

Server = "rest.ensembl.org"
Endpoint = "/info/ping"
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
if person["ping"] == 1:
   print("PING OK! The database is running.")