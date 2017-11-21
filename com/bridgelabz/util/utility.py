import math
import sys


class Utility:

    def checkanagram(self, word1, word2):
        """

        :param word1:
        :type word1:str

        :param word2:
        :type word2:str
        :return:
        """
        count = 0
        len1 = len(word1)
        len2 = len(word2)
        if (len1 != len2):
            return False

        list1 = list(word1)
        list2 = list(word2)
        list1 = self.bubblesort(list1)
        list2 = self.bubblesort(list2)
        for i in range(len1):
            if list1[i] == list2[i]:
                count += 1

        if count == len1:
            return True

        return False

    @staticmethod
    def bubblesort(list3):
        """
        :param list3:
        :type list3:list
        :return: list3
        """
        length = len(list3)

        for i in range(length):
            for j in range(0, length - i - 1):

                if list3[j] > list3[j + 1]:
                    list3[j], list3[j + 1] = list3[j + 1], list3[j]

        return list3

    @staticmethod
    def checkPrime(number):
        """

        :param number:
        :type number:int
        :return:
        :rtype:
        """
        for i in range(2, number):
            if (number % i == 0):
                return False

        return True

    @staticmethod
    def convert(number):
        """

        :param number:
        :type number:int
        :return:list1

        """
        list1 = [int(i) for i in str(number)]
        return list1

    @staticmethod
    def checkpalindrome(word):
        """

        :param word: 
        :type word: 
        :return: 
        :rtype: 
        """
        list1 = list(word);
        j = len(list1) - 1
        i = 0
        while (i < len(list1)):

            if list1[i] != list1[j]:
                return False
            i += 1
            j -= 1
        return True

    def binarySearch(self, list1, low, high, element):

        """

        :param list1:

        :param low:

        :param high:

        :param element:

        :return: mid
        :rtype: int
        """
        mid = int(low + (high - low) / 2)

        if element in list1:

            if (list1[mid] == element and mid>high and mid<low):
                return mid

            elif (list1[mid] < element):
                return self.binarySearch(list1, mid + 1, high, element)
            elif (list1[mid] > element):
                return self.binarySearch(list1, low, mid - 1, element)
            else:
                return -1

        else:
         return "element doestn exist"




    def binarySearchFind(self, low, high):

        """

        :param low:
        :type low:int
        :param high:
        :type:int


        """
        mid = int((low + high) / 2)

        if (low < high):

            print("is your element between", low, mid)
            char = input()

            if (char == 'y'):

                return self.binarySearchFind(low, mid)
            else:

                return self.binarySearchFind(mid + 1, high)
        else:
            print("element is", mid)
            return

    @staticmethod
    def insertionSort(list1):
        """

        :param list1:
        :type list1:list
        :return:
        :rtype:
        """
        for i in range(1, len(list1)):
            key = list1[i]

            j = i - 1
            while (j >= 0 and key < list1[j]):
                list1[j + 1] = list1[j]
                j = j - 1

            list1[j + 1] = key

        return

    def mergeSort(self, list1, low, high):

        """

        :param list1:

        :param low:

        :param high:

        :return:
        :rtype:
        """
        if low < high:
            mid = int((low + (high - 1)) / 2)

            self.mergeSort(list1, low, mid)
            self.mergeSort(list1, mid + 1, high)
            self.merge(list1, low, mid, high)
            return

    def merge(self, list1, low, mid, high):
        """

        :param list1:
        :type list1: list
        :param low:
        :type low:int
        :param mid:
        :type mid: int
        :param high:
        :type high:int
        :return:
        :rtype:
        """
        length1 = mid - low + 1
        length2 = high - mid
        lowarray = [0] * length1
        higharray = [0] * length2
        for i in range(0, length1):
            lowarray[i] = list1[low + i]
        for j in range(0, length2):
            higharray[j] = list1[mid + 1 + j]
        i = 0
        j = 0
        temp = low
        while (i < length1 and j < length2):
            if lowarray[i] <= higharray[j]:
                list1[temp] = lowarray[i]
                i += 1
            else:
                list1[temp] = higharray[j]
                j += 1

            temp = temp + 1

        while (i < length1):
            list1[temp] = lowarray[i]
            temp += 1
            i += 1
        while (j < length2):
            list1[temp] = higharray[j]
            temp += 1
            j += 1

        return

    def findword(self, element):
        """

        :rtype: list
        :param element:

        """
        with open("/home/bridgeit/Desktop/wordlist") as file:
            list1 = file.read().rstrip("\n").split(",")
        self.bubblesort(list1)
        length = len(list1)
        return self.binarySearch(list1, 0, length, element)

    @staticmethod
    def converttobinary(number: int) -> int:
        """

        :param number:
        :type number:int
        :return binary:
        :rtype string:
        """
        bin = ["0", "1"]
        binary = ""
        padding = 0

        while (number > 0 or padding == 0):
            rem = int(number % 2)
            binary = bin[rem] + binary
            number = int(number / 2)
            padding += 1
            if (padding % 4 == 0 and number != 0):
                binary = " " + binary
            if (number == 0):
                while (padding % 8 != 0):
                    if (padding % 4 == 0):
                        binary = " " + binary
                    binary = "0" + binary
                    padding += 1

        return binary

    @staticmethod
    def swapnibble(binary: int) -> int:
        """

        :param binary:
        :type binary:int
        :return:
        :rtype:
        """

        binary = binary.replace(" ", "")
        lowernibble = binary[0:4]
        uppernibble = binary[4:8]
        newbinary = uppernibble + lowernibble
        return newbinary

    @staticmethod
    def binarytodecimal(binary):
        """

               :param binary:
               :type binary:int
               :return:
               :rtype:
               """

        power = 0
        decimal = 0
        length = len(binary) - 1
        while (length >= 0):
            decimal = decimal + int(binary[length]) * math.pow(2, power)
            power += 1
            length -= 1

        return decimal


    def vendingmachine(self, change, index, list1, list2,dlist):




        """

        :param change:
        :type change :int
        :param index:
        :type index:int
        :param list1:
        :type list1:list
        :param list2:
        :type list2:list
        :return:
        :rtype:
        """



        while (index < len(list1) and change != 0):
            if change < int(list1[index]):
                index += 1
                return self.vendingmachine(change, index, list1, list2,dlist)
            else:
                change = change - int(list1[index])
                tempvalue=dlist.__getitem__(list1[index])

                tempvalue += 1

                dlist[list1[index]] = tempvalue
                return self.vendingmachine(change, index, list1, list2,dlist)

        # for i in range(0, len(list1)):
        #     print("note name", list1[i], "note no", list2[i])
        print(dlist)

        return


    @staticmethod
    def bubblesortdesc(list3):
        """

        :param list3:
        :type list3:int
        :return:
        :rtype:
        """
        length = len(list3)

        for i in range(length):
            for j in range(0, length - i - 1):

                if list3[j] < list3[j + 1]:
                    list3[j], list3[j + 1] = list3[j + 1], list3[j]

        return list3


    @staticmethod
    def dayofweek(day: int, month: int, year: int) -> int:
        """

        :param day:
        :type day:int

        :param month:
        :type month:int
        :param year:
        :type year:int
        :return: d0
        :rtype:int
        """

        tempyear = year - (14 - month) / 12
        leap = tempyear + tempyear / 4 - tempyear / 100 + tempyear / 400
        tempmonth = month + 12 * ((14 - month) / 12) - 2
        d0 = int((day + leap + 31 * tempmonth / 12) % 7)
        return d0


    @staticmethod
    def tempconversion(fahr: int, cels: int) -> int:
        C = (fahr - 32) * 5 / 9
        F = (cels * 9 / 5) + 32
        print(C, "celsius", F, "fahrenheit")
        return


    @staticmethod
    def newtonsqrt(number):
        t = number
        while (math.fabs(t - number / t) > sys.float_info.epsilon * t):
            t = ((number / t) + t) / 2

        print(t)
        return

    @staticmethod
    def monthlyPayment(principal,noofyears,rate):
        n=noofyears*12
        r=rate/(12*100)
        payment=float((principal*r)/1-math.pow((1+r),n))
        return payment