from com.bridgelabz.util import utility
import datetime
class TimeSort:
    @staticmethod
    def run():
        listi=[87,65,43,56,23]
        lists=["aashish","sujit","mahesh","sumit"]
        time=[]
        number=int(input("enter number"))
        high=len(listi)
        utility.Utility().bubblesort(listi)
        start = datetime.datetime.utcnow()
        position=utility.Utility().binarySearch(listi,0,high,number)
        stop = datetime.datetime.utcnow()
        print(position)

        elapsedtime = (stop - start).microseconds
        time.append(elapsedtime)
        print("elapsed time in microseconds for  binary integer", elapsedtime)

        string = input("enter string")
        high = len(lists)
        utility.Utility().bubblesort(lists)
        start = datetime.datetime.utcnow()
        position = utility.Utility().binarySearch(lists, 0, high, string)
        stop = datetime.datetime.utcnow()

        print(position)
        elapsedtime = (stop - start).microseconds
        time.append(elapsedtime)
        print("elapsed time in microseconds for  binary string", elapsedtime)

        listi = [87, 65, 43, 56, 23]
        lists = ["aashish", "sujit", "mahesh", "sumit"]
        start = datetime.datetime.utcnow()
        utility.Utility().insertionSort(listi)
        stop = datetime.datetime.utcnow()
        print(listi)
        elapsedtime = (stop - start).microseconds
        time.append(elapsedtime)
        print("elapsed time in microseconds for  insertion integer", elapsedtime)
        start = datetime.datetime.utcnow()
        utility.Utility().insertionSort(lists)
        stop = datetime.datetime.utcnow()
        print(lists)
        elapsedtime = (stop - start).microseconds
        time.append(elapsedtime)
        print("elapsed time in microseconds for  insertion integer", elapsedtime)

        listi = [87, 65, 43, 56, 23]
        lists = ["aashish", "sujit", "mahesh", "sumit"]
        start = datetime.datetime.utcnow()
        utility.Utility().bubblesort(listi)
        stop = datetime.datetime.utcnow()
        print(listi)
        elapsedtime = (stop - start).microseconds
        time.append(elapsedtime)
        print("elapsed time in microseconds for  bubble integer", elapsedtime)

        start = datetime.datetime.utcnow()
        utility.Utility().bubblesort(lists)
        stop = datetime.datetime.utcnow()
        print(lists)
        elapsedtime = (stop - start).microseconds
        time.append(elapsedtime)
        print("elapsed time in microseconds for  bubble integer", elapsedtime)

        print(utility.Utility().bubblesortdesc(time))

        return

TimeSort.run()
