"""

"""

# Utility
from com.bridgelabz.utility.Utility import Utility


def anagram():
    """

    :return:
    """
    utility_obj=Utility()
    print("Enter the frist string:")
    string1=utility_obj.inputString()
    print("Enter the second string:")
    string2=utility_obj.inputString()
    utility_obj.anagramLogic(string1,string2)


# Start execution
if __name__ in '__main__':
    print("Execution start here")
    anagram()



