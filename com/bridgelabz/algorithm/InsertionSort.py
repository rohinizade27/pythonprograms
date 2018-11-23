from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the size of list:")
size=utility_obj.inputIntiger()
insertionlist=[]
print("Enter the string Elements:")
insertionlist=utility_obj.acceptListElement(size)
utility_obj.insertionSortLogic(insertionlist,size)