
"""
purpose   : Hashing Function to search a Number in a slot
@Author   : Rohini Zade
@version  : 1.0
@since    : 1-12-2018

"""

from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *

if __name__ == "__main__":
    utility_obj = Utility()
    hashfunction_object = HashFunction()
    storeelement = [30, 45, 22, 42, 85, 10, 67, 55]
    no_of_slots = 8
    hashlist = hashfunction_object.hashFunctionLogic(no_of_slots, storeelement)
    print(hashlist)
    print("Enter the no you want to search:")
    key = utility_obj.inputIntiger()
    hashfunction_object.hashSearchFunction(key, hashlist, no_of_slots)




