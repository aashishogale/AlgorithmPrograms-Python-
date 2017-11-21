from com.bridgelabz.util import utility


class Primenumber:
    def run(self):
        for i in range(2, 1000):
            if (utility.Utility().checkPrime(i) == True):
                print(i)

        return


primenumber = Primenumber
primenumber.run('self')
