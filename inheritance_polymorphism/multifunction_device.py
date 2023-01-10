class Scanner():
    def scan(self):
        print("scan() from the Scanner class")

class Printer:
    def print(self):
        print("print() from the Printer class")

class Fax:
    def send(self):
        print("send() from the Fax class")

    def print(self):
        print("print() from the Fax class")

class MFD_SPF(Scanner, Printer, Fax):
    def __init__(self):
        pass

class MFD_SFP(Scanner, Fax, Printer):
    def __init__(self):
        pass

spf = MFD_SPF()
sfp = MFD_SFP()

spf.scan()
spf.print()
spf.send()

sfp.scan()
sfp.print()
sfp.send()
