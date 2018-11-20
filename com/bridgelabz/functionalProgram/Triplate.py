from com.bridgelabz.utility.Utility  import Utility

utility_obj=Utility()
print("Enter the size of list:")
size=utility_obj.inputIntiger()
print("Enter element of list:")
listelement=[]
listelement=utility_obj.acceptElement(size)
newlistelement=utility_obj.distinctTriplate(size,listelement)
