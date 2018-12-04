from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the value of a in quadratic expression:")
a=utility_obj.inputIntiger()
print("Enter the value of b in quadratic expression:")
b=utility_obj.inputIntiger()
print("Enter the value of b in quadratic expression:")
c=utility_obj.inputIntiger()

deltaresult=utility_obj.computDelta(a,b,c)
utility_obj.findroots(a,b,c,deltaresult)
