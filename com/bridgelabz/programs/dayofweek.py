from com.bridgelabz.util import utility
class dayofweek:
    def run(self):
        day=int(input("enter day"))
        month=int(input("enter month"))
        year=int(input("enter year"))
        daylist=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
        index=utility.Utility().dayofweek(day,month,year)
        print("the day is ",daylist[index])
        return


dayofweek().run()
