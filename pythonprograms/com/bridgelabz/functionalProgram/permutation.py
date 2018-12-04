from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the string:")
string=utility_obj.inputString()
currentIndex=0
utility_obj.permutationLogic(string,currentIndex)