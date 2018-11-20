import random
import math
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
######################################################################################

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

    def findDistinct(self,number):
        randomnumber = 0
        randomcount = 0
        distinctcount = 0
        count = 0
        flag = 0

        distinctarray=[0]
        while number > distinctcount:
            flag = 0
            randomnumber=random.randrange(0,1000)
            randomcount=randomcount+1
            print(randomcount)
            for i in range(number):
                if distinctarray[i] != randomnumber and 0 < randomnumber:
                    flag = 1

            if flag == 1:
                distinctarray.append(randomnumber)
                count=count+1
                distinctcount=distinctcount+1

        print("Total random numbers required: ",randomcount)
        print("Distinct Coupons are:")
        print(distinctarray)
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
