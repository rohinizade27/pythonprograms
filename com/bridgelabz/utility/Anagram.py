from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *


utility_obj=Utility()
anagram_obj=Anagram()
stackllist=StackByLink()

print("Enter the lower limit:")
lower_limit=utility_obj.inputIntiger()
print("Enter the upper limit:")
upper_limit=utility_obj.inputIntiger()
primenumber=utility_obj.findPrimeNumber(lower_limit,upper_limit)

print("The prime number which are Anagram:")
for i in range(len(primenumber)):
    for j in range(len(primenumber)):
        if primenumber[i] > 0 and primenumber[j] > 0:
            string1 = str(primenumber[i])
            string2 = str(primenumber[j])
            anagram_obj.anagramLogic(string1, string2)



