from com.bridgelabz.utility.Utility  import Utility

template = "hello <<username>>!! how are you?"
print(template)
utility_obj=Utility()
print("Enter the Username:")
username=utility_obj.inputString()
result=utility_obj.replace_string(template,username)
print(result)
