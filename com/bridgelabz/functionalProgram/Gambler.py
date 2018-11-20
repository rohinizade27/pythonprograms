from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the number of trials:")
no_of_trails=utility_obj.inputIntiger()
print("Enter Stake:")
stake=utility_obj.inputIntiger()
print("Enter Goal:")
goal=utility_obj.inputIntiger()
utility_obj.gamblerLogic(no_of_trails,stake,goal)