from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *

utility_obj = Utility()
hashfunction_object=HashFunction()
storeelement=[]

print("Enter the number of slots:")
no_of_slots=utility_obj.inputIntiger()
print("Enter the element you want to store in hashlist")

storeelement=utility_obj.acceptIntegerElement(no_of_slots)
hashfunction_object.hashFunctionLogic(no_of_slots,storeelement)


