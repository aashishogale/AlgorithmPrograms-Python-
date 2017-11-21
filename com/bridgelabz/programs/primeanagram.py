from com.bridgelabz.util import utility


class Primeanagram:
    def run(self):
        for i in range(2, 1000):

            if (utility.Utility().checkPrime(i) == True):
                for j in range(i + 1, 1000):
                    if (utility.Utility().checkPrime(j) == True):
                        

                        if( utility.Utility().checkanagram(str(i),str(j))==True):
                            print(i, j)

        return


primeanagram = Primeanagram
primeanagram.run('self')
