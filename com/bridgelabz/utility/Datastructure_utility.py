class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=Node()

    def append(self,data):
        new_node=Node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return  total

    def display(self):
        elements=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elements.append(cur_node.data)
        print(elements)

    def getindexitem(self,index):
        if index>=self.length():
            print("index out of range")
            return None

        cur_index=0
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            if cur_index==index:
                print("Element at",index,"index is:",cur_node.data)
            cur_index+=1

    def remove(self,index):
        if index>=self.length():
            print("index out of range")
            return
        cur_index=0
        cur_node=self.head
        while cur_node.next != None:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_index==index:
                last_node.next=cur_node.next
                return
            cur_index+=1

    def isempty(self):
        traverse=self.head

        if traverse.next == None:
            print("link list Empty!!!")
        else:
            print("list is not Empty!!!")

    def additematfront(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def searchElement(self, key):
        traverse_pointer = self.head
        while traverse_pointer.next!=None:
            # print(key)
            # print(traverse_pointer.data)
            if traverse_pointer.data == key:
                return True
            traverse_pointer = traverse_pointer.next
            # print(traverse_pointer.data)
        if traverse_pointer.data == key:
            return True
        return False

    def pop(self,data):
        cur_node=self.head
        while cur_node.next != None:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_node.data==data:
                last_node.next=cur_node.next
                return
        return








link_list=Linkedlist()




# # link_list.isempty()
# link_list.append(1)
# link_list.append(2)
# link_list.append(3)
# link_list.append(4)
# link_list.display()
# link_list.remove(0)
# link_list.display()
# link_list.pop(3)
# link_list.display()
#
# # link_list.remove(1)
# # #link_list.additematfront(7)
# # link_list.isempty()
# # #link_list.insert_after_node(1,5)
# # link_list.remove(0)
# print(link_list.searchElement(4))


#link_list.display()


#link_list.getindexitem(1)

# fileobject = open("inputword.txt", "w+")
# list=["rohini ","rajat ","sai ","akansha"]
# fileobject.writelines(list)
# fileobject.close()
#
# fileojbect = open("inputword.txt", "r")
#
# storefilecontent = fileojbect.read()
# storefilecontent=str(storefilecontent).split()
# print(storefilecontent)
# fileojbect.close()
#
# for i in range(len(list)):
#     link_list.append(list[i])
#
# link_list.display()
#
# key=input("Enter the Element you want to search:")
# result=link_list.searchElement(key)
# print(result)
#
# if result==False:
#     link_list.append(key)
# else:
#     link_list.pop(key)
#
# link_list.display()

###########################################################################################

class OrderedLinkList:
    def __init__(self):
        self.head=Node()

    def append(self,data):
        new_node = Node(data)

        traverse_node = self.head

        if traverse_node is None:
            new_node.next = traverse_node
            traverse_node = new_node


        if traverse_node.data >= new_node.data:
            new_node.next =traverse_node
            traverse_node= new_node


        else:

            while traverse_node.next != None and traverse_node.next.data < new_node.data:
                traverse_node.next = new_node
                traverse_node = traverse_node.next
            new_node.next = traverse_node.next
            traverse_node.next = new_node


    def display(self):
        elements=[]
        traverse_node=self.head
        while traverse_node.next!=None:
            traverse_node=traverse_node.next
            elements.append(traverse_node.data)
        print(elements)



#
# ordered_llist=OrderedLinkList()
# ordered_llist.append(4)
# ordered_llist.append(3)
# ordered_llist.append(1)
# ordered_llist.append(-1)
#
# ordered_llist.display()

##################################################################################################

class Stack:
    def __init__(self):
        stackelement=[]
        self.stack=stackelement
        self.top=-1
        self.stackMaxsize=5

    def push(self,data):
        if self.top>=self.stackMaxsize:
            print("Overflow!!! no enough space ")
        else:
            self.top=self.top+1
            self.stack[self. top]=data


    def pop(self):
        if self.top==-1:
            print("Underflow!!! no items in stack")
        else:
            temp=self.stack[self.top]
            self.top-=1
            return temp

    def display(self):
        print(self.stack)

stack_obj=Stack()
stack_obj.push(10)

stack_obj.push(41)
print(stack_obj.pop())
stack_obj.display()






