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
         string1.lower()
         string2.lower()

         flag=0
         if len(string1)==len(string2):
             for i in range(len(string1)):
                 for j in range(len(string1)):
                     if string1[i]==string2[j]:
                         flag=1


         if flag==1:
             print("string is an ANAGRAM")
         else:
             print("string is not an ANAGRAM")

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