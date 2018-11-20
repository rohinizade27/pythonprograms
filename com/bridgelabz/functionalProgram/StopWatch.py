from com.bridgelabz.utility.Utility  import Utility
import time

utility_obj=Utility()
starttime=0
stoptime=0
choice=0
flag=0
print("press 1 to start the stopwatch:")
print("please press 1 ")
choice=utility_obj.inputIntiger()
if choice == 1:
    print("start time:")
    starttime=utility_obj.getstartandstoptime()
    print(starttime)
    choice1=int(input("press 0 to stop:"))
    if choice1==0:
        print("stop time:")
        stoptime=utility_obj.getstartandstoptime()
        print(stoptime)
        flag=1
    else:
        print("invalid input to the stop watch!!")
        flag=0

else:
    print("invalid input to the start watch!!")
    flag=0

if flag==1:
    elapsetime=utility_obj.elapsedTime(starttime,stoptime)
    print("Elapsed time is:", elapsetime)


