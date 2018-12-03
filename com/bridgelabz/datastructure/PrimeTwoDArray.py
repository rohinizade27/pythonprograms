"""
purpose   : print the prime numbers which are anagram from given range in a 2D Array

@Author   : Rohini Zade
@version  : 1.0
@since    : 29-11-2018

"""

from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *

if __name__ == "__main__":
    utility_obj = Utility()

    print("Enter the lower limit:")
    lower_limit = utility_obj.inputIntiger()
    print("Enter the upper limit:")
    upper_limit = utility_obj.inputIntiger()
    primenumber = []
    primenumber = utility_obj.findPrimeNumber(lower_limit, upper_limit)

    twoDarray_obj.primenslots(primenumber)


