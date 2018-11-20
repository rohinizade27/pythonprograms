from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the number of rows:")
rows=utility_obj.inputIntiger()
print("Enter the number of column:")
columns=utility_obj.inputIntiger()
utility_obj.printArray(rows,columns)