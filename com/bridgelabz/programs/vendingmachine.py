from com.bridgelabz.util import utility
class Vending:
    def run(self):
        change=int(input("enter change"))
        list1 = ['1000', '500', '100', '50', '10', '5', '2', '1']
        length = len(list1)
        dlist = {}
        for i in range(0, len(list1)):
            dlist[list1[i]] = 0
        list2 = [0] * length
        utility.Utility().vendingmachine(change,0,list1,list2,dlist)
        return



Vending().run()

