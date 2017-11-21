from com.bridgelabz.util import utility


class Mergesort:
    def run(self):
        list1 = [443, 54, 23, 65, 34]
        length=len(list1)
        utility.Utility().mergeSort(list1, 0, length - 1)
        print(list1)

        return

Mergesort().run()