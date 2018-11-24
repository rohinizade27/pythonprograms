from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the size of list:")
size=utility_obj.inputIntiger()
bubblesortlist=[]
print("Enter the string Elements:")
bubblesortlist=utility_obj.acceptIntegerElement(size)
utility_obj.bubbleSortLogic(bubblesortlist,size)