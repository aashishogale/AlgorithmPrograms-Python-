from com.bridgelabz.util import utility
class Searchword:
    def run(self):
        word=input("enter word")
        print(utility.Utility().findword(word))
        return


Searchword().run()
