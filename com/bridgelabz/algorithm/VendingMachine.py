from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the cash:")
cash=utility_obj.inputIntiger()
count_total_notes=0

utility_obj.vendingMachineLogic(cash,count_total_notes)
