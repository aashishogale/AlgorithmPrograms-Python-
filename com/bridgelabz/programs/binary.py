from com.bridgelabz.util import utility
class Binary:
    def run(self):
        number=int(input("enter number"))
        binary=utility.Utility().converttobinary(number)
        print(binary)
        return



Binary().run()


