"""
purpose   : Read the Text from a file, split it into words and arrange it as Linked List.
            Take a user input to search a Word in the List. If the Word is not found then
            add it to the list,and if it found then remove the word from the List.
            In the end save the list into a file

@Author   : Rohini Zade
@version  : 1.0
@since    : 27-11-2018

"""
from com.bridgelabz.utility.Datastructure_utility import *
if __name__ == "__main__":
    print("This is ordered list program")
    ordered_llist = OrderedLinkList()

    ordered_llist.insertdata(20)
    ordered_llist.insertdata(15)
    ordered_llist.insertdata(10)
    ordered_llist.insertdata(14)
    ordered_llist.insertdata(30)
    ordered_llist.insertdata(50)



    ordered_llist.display()
