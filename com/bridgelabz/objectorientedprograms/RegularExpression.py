"""
purpose   : Use Regex to replace name, full name, Mobile number, and Date with proper value in given string

@Author   : Rohini Zade
@version  : 1.0
@since    : 5-12-2018
"""

from com.bridgelabz.utility.Oops_Utility import RegularExpression

if __name__ == '__main__':
    regex_obj=RegularExpression()
    substitutions=regex_obj.validateUserInputs()
    string=regex_obj.RegularExpressionLogic(substitutions)
    print("**************************final result:**************************************")
    print(string)

