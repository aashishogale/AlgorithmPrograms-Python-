from com.bridgelabz.util import utility




class Anagram:
    def run(self):
        word1=input("enter first word")
        word2=input("enter second word")
        if(utility.Utility().checkanagram(word1,word2)==True):
            print("they are anagram")
        else:
            print("they are not")



anagram=Anagram
anagram.run('self')

