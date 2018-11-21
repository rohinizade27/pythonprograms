from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the lower limit:")
lower_limit=utility_obj.inputIntiger()
print("Enter the upper limit:")
upper_limit=utility_obj.inputIntiger()
primenumber=[]
primenumber=utility_obj.findPrimeNumber(lower_limit,upper_limit)
print("prime numbers are:")
print(primenumber)