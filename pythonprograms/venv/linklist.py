
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self,head=None):
        self.head=head

    def append(self,data):
        new_node=Node(data)

        if self.head != None:
            self.head=new_node

        else:
            last_node=self.head
            while last_node!=None:
                last_node=last_node.next


           # last_node.next=new_node


    def printlinklist(self):

        traverse_pointer=self.head
        while traverse_pointer.next!=None:
            print(traverse_pointer.data)
            traverse_pointer=traverse_pointer.next

        print(traverse_pointer.data)

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("previous node is not present in the list")
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def searchElement(self,key):
        traverse_pointer=self.head
        while traverse_pointer.next!=None:
            if traverse_pointer.data==key:
                print(key,"Element found")
                break
            else:
                print("Element is not present in list")
                break

    def isempty(self):
        if self.head != None:
           print("link list is Empty!!!")
        else:
            pass

    def findLength(self):

        traverse_pointer = self.head
        list_length = 0
        while traverse_pointer.next!= None:
            list_length+=1
        print("link list length:",list_length)









link_list=Linkedlist()
link_list.isempty()
#link_list.findLength()

link_list.append(10)
# link_list.append(4)
# link_list.append(10)
link_list.prepend(6)
link_list.prepend(8)
link_list.prepend(9)
link_list.searchElement(6)
#link_list.insert_after_node(6, 9)

link_list.printlinklist()
























#
#     def display(self):
#         store_link_list_element=[]
#         current_node=self.head
#         while current_node.next!=None:
#             current_node=current_node.next
#             store_link_list_element.append(current_node)
#             print(store_link_list_element)
#
# link_list=Linkedlist()
# link_list.append(4)
# link_list.display()
