from com.bridgelabz.utility.Utility import Utility
from com.bridgelabz.utility.Datastructure_utility import *

if __name__ == "__main__":
    utility_obj=Utility()
    anagram_obj=Anagram()
    q_linklist_obj=QueeByLinklist()

    anagramlist=[]
    storeanagram=[]
    uniquelist=[]

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
                storeanagram=anagram_obj.anagramLogic(string1, string2,anagramlist)
    uniquelist=anagram_obj.unique_list(storeanagram)
    uniquelist = list(map(int, uniquelist))
    sortedlist=uniquelist.sort(reverse=False)
    anagram_obj.QueueOperationOnAnagramlist(uniquelist)