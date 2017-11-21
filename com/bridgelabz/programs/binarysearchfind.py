from com.bridgelabz.util import utility
class FindNumber:
    def run(self):
        number=int(input("enter number"))
        utility.Utility().binarySearchFind(0,number)
        return

FindNumber().run()