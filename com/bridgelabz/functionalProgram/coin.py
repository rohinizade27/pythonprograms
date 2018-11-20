from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the number of trails you want to filp the coin:")
num_of_trails=utility_obj.inputIntiger()
utility_obj.coinfunction(num_of_trails)