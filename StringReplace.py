template = "hello <<username>>!! how are you?"
print(template)
username = str(input("Enter the user name:"))
if len(username) > 3:
    result = str(template.replace("<<username>>", username))
    print(result)
else:
    print("please ensure you have entered string greater 3 char")
