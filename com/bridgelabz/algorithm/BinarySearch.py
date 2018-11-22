from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()

print("Enter the size of list:")
size=utility_obj.inputIntiger()
wordlist=[]
print("Enter the string Elements:")
wordlist=utility_obj.acceptListElement(size)
utility_obj.binarySearch(wordlist)


