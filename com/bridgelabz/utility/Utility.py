import random
import math
from functools import reduce
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
        #newlist=[]
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
                        #print("Entered year is leap year")
                         return True

                    else:
                        #print("Entered year is not leap year")
                         return False
                else:
                    #print("Entered year is not leap year")
                     return True
            else:
                #print("Entered year is leap year")
                return False
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
                 number = number // i

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
    def computDelta(self, a, b, c):
        return b * b - 4 * a * c

    def findroots(self, a, b, deltaresult):
        print("the roots are real and different")
        root1 = (-b + math.sqrt(deltaresult)) / (2 * a)
        root2 = (-b - math.sqrt(deltaresult)) / (2 * a)
        print("root1:",root1)
        print("root2:",root2)

#####################################################################################
    # def permutationLogic(self,string,currentIndex):
    #     if currentIndex == len(string)):
    #
    #         for i in range(len(string)):
    #              string[1]



                            # Algorithm Programs
#####################################################################################

    def anagramLogic(self,string1,string2):
         string1=string1.replace(" ", "" )
         string2=string2.replace(" ", "")

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


         if count==len(str1_removeduplicates) or string1==string2:
             print(string1, "and", string2, " are an Anagram")
         else:
             print(string1, "and", string2, " are an not Anagram")

######################################################################################
    def findPrimeNumber(self, lower_limit, upper_limit):
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

        range = int(math.pow(2,n))

        print("The rang for guessing game is:",1," to ",range)


        low=1
        high=range
        def binarysearch(low,high):

            while low <=high:
                mid = int((high + low) / 2)
                print("Is your guessed number is",mid,"?....","PRESS 1 IF YES ELSE PRESS ANY NUMBER:")
                result=int(input(""))
                if result==1:
                    print(mid ,"is your number..!!!!")
                    exit()
                else:
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

################################################################################################
    def acceptListElement(self,size):
        storeword=[]
        for i in range(size):
            word=input("")
            storeword.append(word)
        return storeword

    def searchElement(self, key, lower_limit, upper_limit, storefilecontent):
        flag=0
        while  lower_limit <= upper_limit:
            mid = (lower_limit + upper_limit) // 2

            if key == storefilecontent[mid]:
                print(key, "found at", mid, " positiom")
                flag=1

            if key<storefilecontent[mid]:
                upper_limit = mid - 1
            else:
                lower_limit = mid + 1

        if flag==0:
            print("The number you want to search is not present in a list")




    def binarySearch(self):

        fileobject = open("BinarySearch.txt", "r+")
        list=["rohini\n","rajat\n","sai\n","akansha\n"]
        fileobject.writelines(list)
        fileobject.close()

        fileojbect = open("BinarySearch.txt", "r")

        storefilecontent = fileojbect.read().splitlines()
        fileojbect.close()
        storefilecontent.sort()

        print(storefilecontent)
        lower_limit = 0
        upper_limit = len(storefilecontent) - 1


        key=input("Enter the Element you want to search:")
        Utility().searchElement(key,lower_limit,upper_limit,storefilecontent)

################################################################################################


    def insertionSortLogic(self,insertionlist,size):
        print("list before sorting:")
        print(insertionlist)
        print("list after sorting:")
        for i in range(1,size):
            for j in range(i):
                if insertionlist[i]<insertionlist[j]:
                    temp= insertionlist[i]
                    insertionlist[i]= insertionlist[j]
                    insertionlist[j]=temp
        print(insertionlist)
##############################################################################################
    def acceptIntegerElement(self, size):
        storeint = []
        for i in range(size):
            word = int(input(""))
            storeint.append(word)
        return storeint

    def bubbleSortLogic(self,bubblesortlist,size):
        print("list before sorting:")
        print(bubblesortlist)
        print("list after sorting:")
        for i in range(0,size):
            for j in range(i+1,size):
                if bubblesortlist[i] > bubblesortlist[j]:
                    temp = bubblesortlist[i]
                    bubblesortlist[i] = bubblesortlist[j]
                    bubblesortlist[j] = temp
        print(bubblesortlist)
##############################################################################################

    def mergeSortLogic(self, mergesortlist):
        while len(mergesortlist)!=0:
            leftlist = []
            rightlist = []
            # print(mergesortlist)

            if len(mergesortlist) == 0 or len(mergesortlist) == 1:
                print(mergesortlist)
            else:
                lower_limit = 0
                higher_limit = len(mergesortlist) - 1
                mid = (lower_limit + higher_limit) // 2
                for i in range(mid + 1):
                    leftlist.append(mergesortlist[i])

                for j in range(mid + 1, higher_limit + 1):
                     rightlist.append(mergesortlist[j])

              #  print("left list:", leftlist)
               # print("right list:", rightlist)

           # self.mergeSortLogic(leftlist)
            #self.mergeSortLogic(rightlist)
            Utility().sortlists(leftlist,rightlist)

    def sortlists(self,leftlist,rightlist):
        newmergelist=[]

        i=0
        j=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                newmergelist.append(leftlist[i])
                i=i+1
            else:
                newmergelist.append(rightlist[j])
                j=j+1


        while i<len(leftlist):
            newmergelist.append(leftlist[i])
            i=i+1

        while j<len(rightlist):
            newmergelist.append(leftlist[i])
            j=j+1

        print(newmergelist)

###########################################################################################
    def vendingMachineLogic(self,cash,count_total_notes):
        print("cash count:",count_total_notes)
        print("remaining cash:",cash)

        noteslist=[1000, 500, 100, 50, 10, 5, 2, 1]


        while cash>=1 or cash !=1:

            if cash >= noteslist[0]:
                newcash = cash % 1000
                thousand_count=cash//1000
                count_total_notes = count_total_notes +thousand_count
                print(thousand_count,": 1000's notes")
                self.vendingMachineLogic(newcash,count_total_notes)

            elif cash >= noteslist[1]:
                newcash = cash % 500
                fivehundread_count=cash//500
                count_total_notes = count_total_notes + fivehundread_count
                print(fivehundread_count, ":500's notes")
                self.vendingMachineLogic(newcash,count_total_notes)

            elif cash >= noteslist[2]:
                newcash= cash % 100
                hundread_count=(cash//100)
                count_total_notes = count_total_notes + hundread_count
                print(hundread_count, ":100's notes")
                self.vendingMachineLogic(newcash,count_total_notes)

            elif cash >= noteslist[3]:
                newcash = cash % 50
                fifty_count=(cash//50)
                count_total_notes = count_total_notes + fifty_count
                print(fifty_count, ":50's notes")
                self.vendingMachineLogic(newcash,count_total_notes)

            elif cash >= noteslist[4]:
                newcash = cash % 10
                ten_count=cash//10
                count_total_notes = count_total_notes + ten_count
                print(ten_count, ":10's notes")
                self.vendingMachineLogic(newcash,count_total_notes)

            elif cash >= noteslist[5]:
                newcash = cash % 5
                five_count=cash//5
                count_total_notes = count_total_notes + five_count
                print(five_count, ":5's notes")
                self.vendingMachineLogic(newcash,count_total_notes)

            elif cash >= noteslist[6]:
                newcash = cash % 2
                two_count=cash//2
                count_total_notes = count_total_notes + two_count
                print(two_count, ":2's notes")
                self.vendingMachineLogic(newcash,count_total_notes)

            elif cash >= noteslist[7]:
                newcash = cash % 1
                one_count=cash//1
                print(one_count, ":1's notes")
                count_total_notes = count_total_notes + one_count
                print(count_total_notes)
                self.vendingMachineLogic(newcash,count_total_notes)


            else:
                pass

##########################################################################################

    def calculateDayOfWeek(self,day,month,year):
        y=year-(14-month)//12
        x=y+y//4-y//100+y//400
        m=month+12*((14-month)//12)-2
        d=int((day+x+31*m//12)%7)

        return d
##########################################################################################

    def convertTempToCelcius(self,fahrenheit_Temprature):
        # (°F − 32) x 5 / 9 = °C
        #
        # (°C × 9 / 5) + 32 = °F
        tocelius=(fahrenheit_Temprature-32)*5/9
        print("Temprature in Celcius:",tocelius)

    def convertTempTofahrenheit(self,celcius_temprature):
        toFahrenheit=(celcius_temprature*9/5)+32
        print("Temprature in Fahrenheit:",toFahrenheit)

############################################################################################

    def findMonthlyPayment(self,p,y,r):
        n=12*y
        r=r/(12*100)
        payment=((p*r)/1-(1+r)**(-n))
        print("Monthly payment is:",payment)

##########################################################################################
    def newtonSqrtLogic(self,c):
        t=c
        epsilon = 1e-15
        while math.fabs(t - c//t) > epsilon*t:
            t=(c//t+t)//2
        print("value of t:",t)
###########################################################################################
    def decimalToBinary(self,Decimalnumber):
        binarylist=[]
        while Decimalnumber!=0:
            r=Decimalnumber%2
            binarylist.append(str(r))
            Decimalnumber=Decimalnumber//2

        binarylist.reverse()
        return binarylist


##########################################################################################

    def swapBinary(self,binary_number):
        print(binary_number)
        binary_number=''.join(binary_number)
        print("Binary number is:",binary_number)

        binary_number = binary_number.zfill(8)
        print("number_after_padding:",binary_number)

        # total_length=8
        # binary_number_legth=len(binary_number)
        # zero_padding_number=total_length-binary_number_legth
        # print("zero_padding_number:",zero_padding_number)

        nibble_length = len(binary_number) // 2
        print("nibble length:", nibble_length)
        left_nibble = str(binary_number[0:nibble_length])
        right_nibble = str(binary_number[nibble_length:])
        print(left_nibble, right_nibble)
        # for i in range(nibble_length):
        #     for j in range(nibble_length):
        temp = left_nibble
        left_nibble = right_nibble
        right_nibble = temp

        print("left nibble:",left_nibble)
        print("right nibble:",right_nibble)
        binary_number = str(left_nibble + right_nibble)
        print("binary number after swapping:", binary_number)


        binary_number=binary_number.split(",")

        # e=7
        # decimal_number=''
        # for i in range(8):
        #
        #     decimal_number=decimal_number+str((binary_number[0][i]*pow(2,e)))
        #     e=e-1
        # print(decimal_number)
        # decimal = 0
        # i = 1
        # n=[]
        # n=binary_number
        # while n != 0:
        #     r = n % 2
        #     decimal= decimal + r * i
        #     n = n // 10
        #     i = i*2
        #     print(decimal)

#####################################################################################
                    #Data structure Programs

#####################################################################################


































