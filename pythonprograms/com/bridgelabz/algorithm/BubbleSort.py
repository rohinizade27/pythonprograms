from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the size of list:")
size=utility_obj.inputIntiger()
bubblesortlist=[]
print("Enter the Elements:")
bubblesortlist=utility_obj.acceptIntegerElement(size)
starttime = utility_obj.getstartandstoptime()
utility_obj.bubbleSortLogic(bubblesortlist,size)
stoptime=utility_obj.getstartandstoptime()
elapsetime=utility_obj.elapsedTime(starttime,stoptime)
print("Elapsed time is:", elapsetime)