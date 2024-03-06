import termcolor
import socket
class SeqServer:
    def __init__(self):
        self.PORT = 8080
        self.IP = "127.0.0.1"
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ls.bind((self.IP, self.PORT))
        ls.listen()
        print("SEQ Server configured!")
        try:
            while True:
                print("Waiting for clients...")
                (rs, address) = ls.accept()
                msg = rs.recv(2048).decode("utf-8")
                response = self.return_response(str(msg))
                send_bytes = str.encode(response)
                rs.send(send_bytes)
                rs.close()
        except KeyboardInterrupt:
            pass
        ls.close()

    def return_response(self, msg):
        if msg == "PING":
            termcolor.cprint("PING command!", "green")
            return self.ping_response()


    def ping_response(self):
        return "OK!\n"




s = SeqServer()
print(s)