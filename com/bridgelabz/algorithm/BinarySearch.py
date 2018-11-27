from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()

# print("Enter the size of list:")
# size=utility_obj.inputIntiger()
# wordlist=[]
# print("Enter the string Elements:")
#wordlist=utility_obj.acceptListElement(size)
starttime = utility_obj.getstartandstoptime()
utility_obj.binarySearch()
stoptime=utility_obj.getstartandstoptime()
elapsetime=utility_obj.elapsedTime(starttime,stoptime)
print("Elapsed time is:", elapsetime)


