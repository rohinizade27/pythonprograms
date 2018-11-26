from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the Decimal number:")
Decimalnumber=utility_obj.inputIntiger()
binary_number=utility_obj.decimalToBinary(Decimalnumber)
print(binary_number)