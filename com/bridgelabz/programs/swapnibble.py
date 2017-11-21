from com.bridgelabz.util import utility
class Swapnibble:
    def run(self):
        number=int(input("enter number"))
        binary=utility.Utility().converttobinary(number)
        print("binary",binary)
        afterswapped=utility.Utility().swapnibble(binary)
        print("after swapping",afterswapped)
        decimal=utility.Utility().binarytodecimal(afterswapped)
        print(decimal)
        return


Swapnibble().run()