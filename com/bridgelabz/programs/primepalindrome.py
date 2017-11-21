from com.bridgelabz.util import utility
class Primepalindrome:
    def run(self):

        for i in range(10, 1000):

            if (utility.Utility().checkPrime(i) == True):
                if (utility.Utility().checkpalindrome(str(i))==True):
                        print(i)

        return


primepalindrome=Primepalindrome
primepalindrome.run('self')