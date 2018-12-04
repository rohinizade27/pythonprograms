from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the size of list:")
size=utility_obj.inputIntiger()
mergesortlist=[]
print("Enter the Elements:")
mergesortlist=utility_obj.acceptIntegerElement(size)
utility_obj.mergeSortLogic(mergesortlist)