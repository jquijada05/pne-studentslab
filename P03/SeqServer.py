import termcolor
import socket
from Seq1 import Seq
class SeqServer:
    def __init__(self):
        self.PORT = 8081
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
            return self.ping_response()
        elif msg.startswith("GET"):
            return self.get_response(msg)
        elif msg.startswith("INFO"):
            return self.get_info(msg)
        elif msg.startswith("COMP"):
            return self.get_comp(msg)
        elif msg.startswith("REV"):
            return self.get_rev(msg)

    def ping_response(self):
        termcolor.cprint("PING command!", "green")
        print("OK!")
        return "OK!\n"

    def get_response(self, msg):
        termcolor.cprint("GET", "green")
        sequences = ["TCAGTCAA", "CGATACGA", "CCAGTGCA", "TTTCAGTA", "CATGCTAG"]
        for i in msg:
            if i.isdigit():
                if 0 <= int(i) <= 4:
                    n = sequences[int(i)]
                    print(n)
                    return n
                else:
                    return "No sequence exists for this number"


    def get_info(self, msg):
        termcolor.cprint("INFO", "green")
        sequence = Seq(msg.replace("INFO", "").strip())
        info = f"Sequence: {sequence}\n"
        info += f"Total length: {sequence.len()}\n"
        for base in ["A", "C", "G", "T"]:
            count = sequence.count_base(base)
            percentage = count / sequence.len() * 100 if sequence.len() > 0 else 0
            info += f"{base}: {count} ({percentage}%)\n"
        print(info)
        return info

    def get_comp(self, msg):
        termcolor.cprint("COMP", "green")
        sequence = Seq(msg.replace("COMP", "").strip())
        comp = f"{sequence.complement()}"
        print(comp)
        return comp

    def get_rev(self, msg):
        termcolor.cprint("REV", "green")
        sequence = Seq(msg.replace("REV", "").strip())
        rev = f"{sequence.reverse()}"
        print(rev)
        return rev


s = SeqServer()
print(s)