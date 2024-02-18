class Seq:

    def __init__(self, strbases):
        bases = ["A", "C", "G", "T"]
        for i in strbases:
            if i not in bases:
                self.strbases = "ERROR!!"
                print("ERROR!!")
                return
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)