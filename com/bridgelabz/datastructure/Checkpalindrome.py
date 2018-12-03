"""
purpose   : To implement a program to check given string is palindrome or not

@Author   : Rohini Zade
@version  : 1.0
@since    : 28-11-2018

"""

from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *

if __name__ == "__main__":
    utility_obj = Utility()
    queue_obj=Queue()
    palindrome_obj=checkpalindrome()
    string = input("Enter the siring:")
    palindrome_obj.palindromeLogic(string)


