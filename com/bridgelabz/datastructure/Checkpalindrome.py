from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *



if __name__ == "__main__":
    utility_obj = Utility()
    queue_obj=Queue()
    palindrome_obj=checkpalindrome()
    string = input("Enter the siring:")
    palindrome_obj.palindromeLogic(string)


