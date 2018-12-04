from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the size of list:")
size=utility_obj.inputIntiger()
insertionlist=[]
print("Enter the string Elements:")
insertionlist=utility_obj.acceptListElement(size)
starttime = utility_obj.getstartandstoptime()
utility_obj.insertionSortLogic(insertionlist,size)
stoptime=utility_obj.getstartandstoptime()
elapsetime=utility_obj.elapsedTime(starttime,stoptime)
print("Elapsed time is:", elapsetime)