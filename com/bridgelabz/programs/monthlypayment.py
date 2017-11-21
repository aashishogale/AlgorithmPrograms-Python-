from com.bridgelabz.util import utility
class Payment:
    def run(self):
        principal=float(input("enter principal"))
        rate=float(input("enter rate"))
        year=float(input("enter year"))
        payment=utility.Utility.monthlyPayment(principal,year,rate)
        print(payment)
        return

Payment().run()