from com.bridgelabz.utility.Oops_Utility import RegularExpression

if __name__ == '__main__':
    regex_obj=RegularExpression()
    substitutions=regex_obj.validateUserInputs()
    #print(user_name,user_fullname,user_mob_no,curr_date)
    string=regex_obj.RegularExpressionLogic(substitutions)
    print("**************************final result:**************************************")
    print(string)

