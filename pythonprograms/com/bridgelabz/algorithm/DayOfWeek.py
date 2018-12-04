from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the day:")
day=utility_obj.inputIntiger()
print("Enter the month:")
month=utility_obj.inputIntiger()
print("Enter the year:")
year=utility_obj.inputIntiger()

result=utility_obj.calculateDayOfWeek(day,month,year)
daylist=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
print(daylist[result])

