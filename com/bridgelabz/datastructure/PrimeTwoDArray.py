from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *

utility_obj = Utility()

print("Enter the lower limit:")
lower_limit=utility_obj.inputIntiger()
print("Enter the upper limit:")
upper_limit=utility_obj.inputIntiger()
primenumber=[]
primenumber=utility_obj.findPrimeNumber(lower_limit,upper_limit)

# print("Enter the number of rows:")
# rows=utility_obj.inputIntiger()
# print("Enter the number of column:")
# columns=utility_obj.inputIntiger()
# utility_obj.printArray(rows,columns)


twoDarray_obj.primenslots(primenumber)
