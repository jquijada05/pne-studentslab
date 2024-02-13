class Seq:

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        bases = ["A", "C", "G", "T"]
        for i in strbases:
            if i not in bases:
                print("ERROR!!")
                return
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        if self.strbases:
            result = self.strbases
        else:
            result = "ERROR"
        return result

    def len(self):
        return len(self.strbases)

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
