import random
import math
from time import time

import array as arr
import sys

class Utility:
    def __init__(self):
        pass

    def inputString(self):
        string=input("")
        return string

    def inputIntiger(self):
        return int(input(""))


    def replace_string(self,template,username):
        if len(username) > 3:
            result = str(template.replace("<<username>>", username))
            return result
        else:
            print("please ensure you have entered string greater 3 char")
####################################################################################

    def gamblerLogic(self,no_of_trails,stake,goal):
        wincount = 0
        losscout = 0
        if goal < stake:
             num=int(input("number of trails:"))
             newgoal=int(input("Again enter your new goal:"))
             newstake=int(input("Enter stake:"))
             gamblerLogic(num,newgoal,newstake)
        else:
            for i in range(0,no_of_trails):
                cash=stake
                while cash>0 and cash<goal:
                    if random.random()<0.5:
                         cash=cash+1
                    else:
                         cash=cash-1

                if cash==goal:
                    wincount=wincount+1
                else:
                    losscout=losscout+1

        print("wincount:",wincount)
        print("percentage of game won:",(wincount*100)/no_of_trails)
        print("percentage of game loss:",(losscout*100)/no_of_trails)

##############################################################################

    def findDistinct(self, num_of_trails):

        randomcount = 0
        distinctcount = 0
        count = 0

        distinctlist=[]
        while num_of_trails > distinctcount:
            flag =0
            randomnumber=random.randint(1, 1000)
            randomcount=randomcount+1
            print(randomnumber)
            for i in range(num_of_trails):
                if randomnumber not in  distinctlist:
                    distinctlist.append(randomnumber)

            distinctcount = distinctcount + 1

        print("Total random numbers required: ",randomcount)
        print("Distinct Coupons are:")
        print(distinctlist)
#####################################################################################
    def acceptElement(self,size):
        storeElement=[]
        for i in range(size):
            n=int(input(""))
            storeElement.append(n)

        return storeElement

    def distinctTriplate(self,size,listelement):
        #print(listelement)
        #print(size)
        newlist=[]
        flag=0
        for i in range(0,size-2):
            for j in range(i+1,size-1):
                for k in range(j+1,size):
                    if listelement[i]+listelement[j]+listelement[k]==0:
                        print(listelement[i],listelement[j],listelement[k])

                        flag=1


        if flag==0:
            print("Distinct Triplate Doesn't Exist")


################################################################################

    def FindEuclideanDistance(self,x,y):
        Result1 =math.pow(x,x)
        Result2 = math.pow(y,y)
        distance = math.sqrt(Result1 + Result2)
        return distance
##############################################################################

    def coinfunction(self,num_of_trails):
         headcount = 0
         tailcount = 0
         for i in range(num_of_trails):
             random_number = random.random()
             print(random_number)
             if random_number > 0.5:
                 headcount = headcount + 1
             else:
                 tailcount = tailcount + 1

         headpercent = (headcount * 100) / num_of_trails
         print("Head percentage:")
         print(headpercent)
         tailpercent = (tailcount * 100) / num_of_trails
         print("Tail percentage:")
         print(tailpercent)

         if headpercent > tailpercent:
             print("Head percentage is greater")
         else:
             print("tail percentage is greater")

################################################################################

    def HarmonicSeriesfunction(self,number):
        result = 0.0
        while number > 0:
            result = float(result + 1 / number)
            number = number - 1

        print("Harmonic value:", str(result))

###############################################################################

    def leapYearFunction(self,year):
        if len(year) < 4:
            print("please ensure you have entered 4 digit number")
            newyear = input("Enter The Year:")
            leapYearFunction(newyear)
        else:
            if (int(year) % 400 == 0):
                if (int(year) % 100 == 0):
                    if (int(year) % 4 == 0):
                        print("Entered year is leap year")

                    else:
                        print("Entered year is not leap year")
                else:
                    print("Entered year is not leap year")
            else:
                print("Entered year is leap year")
        return

###############################################################################
    def findPrimeFactor(self,number):
         factors = []
         primefactors = []
         isprime = 0
         for i in range(2, int(number + 1)):
             while number % i == 0:
                 factors.append(i)
                 print(" ", i)
                 number = number / i

         for i in range(0, len(factors)):
             if factors[i] == 2:
                 primefactors.append(factors[i])
             else:
                 for j in range(2, factors[i]):

                     if factors[i] % j == 0:
                         isprime = 0
                         break
                     else:
                         isprime = 1
                 if isprime == 1:
                     primefactors.append(factors[i])

         print(primefactors)

######################################################################################
    def printArray(self,rows,columns):
        matrix = []
        print("Enter the values of row:")
        for i in range(rows):
            rows = []
            for j in range(columns):
                values = input("")
                rows.append(values)
            matrix.append(rows)

        fileojbect = open("printarray.txt", "w")
        fileojbect.write(str(matrix))
        fileojbect.close()
        print(matrix)

#######################################################################################
    def getstartandstoptime(self):
        current_time =time()
        return current_time

    def elapsedTime(self,starttime,stoptime):
        elapsed_time=stoptime-starttime
        return elapsed_time

######################################################################################
    def computDelta(self,a,b,c):
        return b * b - 4 * a * c

    def findroots(self,a,b,c,deltaresult):
        print("the roots are real and different")
        root1 = (-b + math.sqrt(deltaresult)) / (2 * a)
        root2 = (-b - math.sqrt(deltaresult)) / (2 * a)
        print("root1:",root1)
        print("root2:",root2)

#####################################################################################
                            # Algorithm Programs
#####################################################################################
    def anagramLogic(self,string1,string2):
         string1=string1.replace(" ","" )
         string2=string2.replace(" ","")

         lowercasestring1 = string1.lower()
         lowercasestring2 = string2.lower()

         str1_removeduplicates="".join(set(lowercasestring1))
         str2_removeduplicates = "".join(set(lowercasestring2))

         count=0
         if len( str1_removeduplicates)==len(str2_removeduplicates):
             for i in range(len(str1_removeduplicates)):
                 for j in range(len(str1_removeduplicates)):
                     if str1_removeduplicates[i]== str2_removeduplicates[j]:
                         count=count+1


         if count==len(str1_removeduplicates):
             print(string1,"and",string2," are an Anagram")
         else:
             print(string1,"and",string2," are an not Anagram")

######################################################################################
    def findPrimeNumber(self,lower_limit,upper_limit):
         storeprime=[]

         i=lower_limit

         for i in range(upper_limit):
             isprime = False
             if i==0 and i==1:
                 continue
             for j in range(2,i):
                 if i % j == 0:
                     isprime = False
                     break
                 else:
                     isprime = True

             if isprime == True:
                 storeprime.append(i)

         return storeprime
###########################################################################################
    def checkPalindrome(self, primenumber):
        for i in range(len(primenumber)):
            reversenum = 0
            if primenumber[i] > 0:
                temp = primenumber[i]
                while temp > 0:
                    r = temp % 10
                    temp = temp // 10
                    reversenum = reversenum * 10 + r
                temp = primenumber[i]
                if temp == reversenum:
                    print(reversenum," is a palindrome")

    def checkAnagram(self,primenumber):
        print("The prime number which are Anagram:")
        for i in range(len(primenumber)):
            for j in range(len(primenumber)):
                if primenumber[i] > 0 and primenumber[j] > 0:
                    string1=str(primenumber[i])
                    string2=str(primenumber[j])
                    self.anagramLogic(string1,string2)

#####################################################################################
    def guessingGameLogic(self,n):
        storerange = []
        range = int(math.pow(2,n))

        print("The rang for guessing game is:",1," to ",range)


        low=1
        high=range
        def binarysearch(low,high):



            while low < high:
                mid = int((high + low) / 2)
                if high - low == 1:
                    print(mid)

                print("Guess the number:")
                print("1)Range is:",low ,"to",mid)
                print("2)Range is:",mid+1, "to",high)
                guess_number=int(input("In which range number is present..??"))

                if guess_number==1:
                    binarysearch(low,mid-1)
                elif guess_number==2:
                    binarysearch(mid+1,high)
                else:
                    print("!!!..wrong choice..!!!")


        binarysearch(low,high)











