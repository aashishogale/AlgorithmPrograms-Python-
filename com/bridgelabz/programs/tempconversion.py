from com.bridgelabz.util import utility
class Tempconversion:

    def run(self):
        cel=int(input("enter temp in celsius"))
        fahr=int(input("enter temp in fahr"))
        utility.Utility().tempconversion(fahr,cel)
        return



Tempconversion().run()