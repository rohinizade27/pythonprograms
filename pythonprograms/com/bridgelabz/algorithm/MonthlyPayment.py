from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter principle amount:")
p=utility_obj.inputIntiger()
print("Enter the no of years:")
y=utility_obj.inputIntiger()
print("Enter the rate of interset:")
r=utility_obj.inputIntiger()
utility_obj.findMonthlyPayment(p,y,r)


