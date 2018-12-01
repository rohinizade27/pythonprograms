import numpy as np
import math

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
    top = 0
    stackMaxsize = 10

    def __init__(self):

        self.stack=list()


    def push(self,data):
        if len(self.stack)>self.stackMaxsize:
            print("Overflow!!! no enough space ")
        else:
            tp=self.top
            tp+=1
            self.stack.insert(tp,data)
            #self.stack[tp]=data



    def pop(self):

        if self.stack==[]:
            print("Underflow!!! no items in stack")
        else:
            tp = self.top
            temp=self.stack[tp]
            self.stack.pop()
            tp-=1
            return temp

    def isempty(self):
        if self.stack==[]:

            return True


    def display(self):
        print(self.stack)

# stack_obj=Stack()
# # stack_obj.push(10)
# # stack_obj.push(41)
# # stack_obj.push(90)
# #
# # stack_obj.pop()
# # stack_obj.pop()
# # stack_obj.pop()
# # stack_obj.pop()
# # stack_obj.push(20)
# # stack_obj.display()
#
# expression=input("Enter the Expression:")
# balance=True
# for i in range(len(expression)):
#     if expression[i]=='(':
#         stack_obj.push(i)
#
#     else:
#         if stack_obj.isempty():
#             balance=False
#         else:
#             if expression[i]==')':
#                 stack_obj.pop()
#
# result=stack_obj.isempty()
#
# if result==True and balance==True:
#     print("Expression is blanced..!!!")
# else:
#     print("expression is not balanced..!!")

##########################################################################################
class Queue:
    def __init__(self):
        self.queue=list()



    def insertElement(self,data,maxlen):
        rear=len(self.queue)
        rear=rear+1

        #print(rear)
        if rear>maxlen:
            print("Overflow!!..no enough space..!!")
            exit()
        else:
            self.queue.append(data)

    def deleteElement(self):
        if queue_obj.isEmpty():
            print("Underflow!!..No Elements on stack!!")
            exit()
        else:
            self.queue.pop(0)

    def isEmpty(self):
        if self.queue==[]:
            return True

    def display(self):
        print(self.queue)

    def withdraw(self,available_balance):
        withdraw_cash = int(input("please Enter the withdraw amount:"))
        if available_balance >= withdraw_cash:
            available_balance -= withdraw_cash
            print("Available Balance:", available_balance)
            print("Withdraw Amount:", withdraw_cash)
            queue_obj.deleteElement()
            #queue_obj.display()

        else:
            print("SORRY !!! Insufficient Balance..!!")
            queue_obj.deleteElement()
            #queue_obj.display()

    def deposit(self,available_balance):
        deposit_cash=int(input("Enter the deposit amount:"))
        available_balance+=deposit_cash
        print("Available Balance:", available_balance)
        print("Withdraw Amount:", deposit_cash)
        queue_obj.deleteElement()
        queue_obj.display()




queue_obj=Queue()
# # queue_obj.insertElement(10)
# # queue_obj.insertElement(20)
# # queue_obj.insertElement(30)
# # queue_obj.insertElement(45)
# # queue_obj.insertElement(65)
# #queue_obj.insertElement(90)
# # queue_obj.insertElement(90)
# # queue_obj.deleteElement()
# # queue_obj.deleteElement()
#
# #queue_obj.deleteElement()
# #queue_obj.display()
#
# available_balance=500000
# maxlen=int(input("How may persons are there in a Queue?"))
# print("people in queue:")
# for i in range(maxlen):
#     person_id=input("please enter the id of person:")
#     queue_obj.insertElement(person_id,maxlen)
#
#
# for i in range(maxlen):
#     queue_obj.display()
#     print("___You have two choices___")
#     print("1. withdraw Cash")
#     print("2. Deposit cash")
#     ch = int(input("Enter your choice:"))
#     if ch == 1:
#         queue_obj.withdraw(available_balance)
#     elif ch == 2:
#         queue_obj.deposit(available_balance)
#     else:
#         print("!!..Invalid choice..!!")

###########################################################################################
class checkpalindrome:
    def __init__(self):
        pass

    def palindromeLogic(self,string):
        stringlist = []
        for i in range(len(string)):
            stringlist.append(string[i])

        for i in range(len(string)):
            dequeue_obj.insertElementAtRear(string[i], len(string))

        storelement=dequeue_obj.dequeue

        reverselist = []
        for j in range(len(storelement)):
            element=dequeue_obj.deleteElementfromRear()
           #print(element)
            reverselist.append(element)
        print("original string:",stringlist)
        print("reverse string:",reverselist)
        if stringlist == reverselist:
            print("string is palindrome")
        else:
            print("string is not palindrome")


#############################################################################
class Dequeue:
    def __init__(self):
        self.dequeue=list()



    def insertElementAtRear(self,data,maxlen):
        rear=len(self.dequeue)
        rear=rear+1

        #print(rear)
        if rear>maxlen:
            print("Overflow!!..no enough space..!!")
            exit()
        else:
            self.dequeue.append(data)

    def insertElementAtFront(self,data,maxlen):
        rear = len(self.dequeue)
        rear = rear + 1

        if rear>maxlen:
            print("Overflow!!..no enough space..!!")
            exit()
        else:
            self.dequeue.insert(0,data)



    def deleteElementfromfront(self):
        if dequeue_obj.isEmpty():
            print("Underflow!!..No Elements on stack!!")
            exit()
        else:
            self.dequeue.pop(0)

    def deleteElementfromRear(self):
        rear = len(self.dequeue)
        rear = rear-1
        #print(rear)
        if dequeue_obj.isEmpty():
            print("Underflow!!..No Elements on stack!!")
            exit()
        else:
            return self.dequeue.pop(rear)



    def isEmpty(self):
        if self.dequeue==[]:
            return True

    def display(self):
        print(self.dequeue)

# maxlen=5
# dequeue_obj=Dequeue()
# dequeue_obj.insertElementAtRear(10,maxlen)
# dequeue_obj.insertElementAtRear(11,maxlen)
# dequeue_obj.insertElementAtFront(21,maxlen)
# dequeue_obj.insertElementAtFront(26,maxlen)
# dequeue_obj.deleteElementfromfront()
# dequeue_obj.deleteElementfromRear()
# dequeue_obj.insertElementAtFront(28,maxlen)
# dequeue_obj.deleteElementfromRear()
#dequeue_obj=Dequeue()

##############################################################################
class Anagram:

    def anagramLogic(self,string1,string2,anagramlist):

         string1=string1.replace(" ", "" )
         string2=string2.replace(" ", "")

         lowercasestring1 = string1.lower()
         lowercasestring2 = string2.lower()

         str1_removeduplicates="".join(set(lowercasestring1))
         str2_removeduplicates = "".join(set(lowercasestring2))

         count=0
         if len( str1_removeduplicates)==len(str2_removeduplicates):
             for i in range(len(str1_removeduplicates)):
                 for j in range(len(str1_removeduplicates)):
                     if str1_removeduplicates[i]== str2_removeduplicates[j]:
                         count=count+1


         if count==len(str1_removeduplicates) or string1==string2:



             anagramlist.append(string2)


         else:
             pass

         return anagramlist
             # # print(string1, "and", string2, " are an Anagram")
         # else:
         #     # print(string1, "and", string2, " are an not Anagram")
         #     pass

    def unique_list(self,storeanagram):
        uniq_list = []
        uniq_set = set()
        for item in storeanagram:
            if item not in uniq_set:
                uniq_list.append(item)
                uniq_set.add(item)
        return uniq_list

    def stackOperationOnAnagramlist(self,uniquelist):
        popedElement=[]
        print("Anagram number after pushed it into stack...")
        for i in range(len(uniquelist)):
            stackllist.push(uniquelist[i])
        stackllist.display()

        print("Anagram number after poped it from stack...")
        for i in range(len(uniquelist)):
            item=stackllist.pop()
            popedElement.append(item)
        #stackllist.display()
        print(popedElement)

    def QueueOperationOnAnagramlist(self,uniquelist):
        deletedElement=[]
        print("Anagram number after inserted into queue...")
        for i in range(len(uniquelist)):
            q_linklist_obj.insertElementAtRear(uniquelist[i])
        q_linklist_obj.display()

        print("Anagram number after deleted from queue...")
        for i in range(len(uniquelist)+1):
            item = q_linklist_obj.removeElementFromFront()
            deletedElement.append(item)
        # stackllist.display()
        print(deletedElement)



###################################################################################
class StackByLink:

    def __init__(self):
        self.head=Node()

    def push(self, data):
        new_node = Node(data)
        traverse= self.head
        while traverse.next != None:
            traverse = traverse.next
        traverse.next = new_node



    def display(self):
        elements=[]
        traverse=self.head
        while traverse.next!=None:
            traverse=traverse.next
            elements.append(traverse.data)
        print(elements)


    def pop(self):
        traverse=self.head

        if traverse.next==None:
            print("Underflow..!!")


        while traverse.next != None:
            t=traverse.next
            if t.next ==None:
                traverse.next=None
                return t.data
            traverse=traverse.next

    def isUnderflow(self):
        traverse = self.head
        if traverse.next == None:
            return True
        else:
            return False


stackllist=StackByLink()
# stackllist.push(10)
# stackllist.push(20)
# stackllist.pop()
# stackllist.pop()
# stackllist.pop()
# print(stackllist.isUnderflow())
# stackllist.display()
############################################################################################
class QueeByLinklist:
    def __init__(self):
        self.head=Node()

    def insertElementAtRear(self, data):
        new_node = Node(data)
        traverse= self.head
        while traverse.next != None:
            traverse = traverse.next
        traverse.next = new_node

    def removeElementFromFront(self):
        if self.head is None:
            return None

        else:
            pop_node= self.head.data
            self.head = self.head.next
            return pop_node

    def display(self):
        elements=[]
        traverse=self.head
        while traverse.next!=None:
            traverse=traverse.next
            elements.append(traverse.data)
        print(elements)

q_linklist_obj=QueeByLinklist()
# q_linklist_obj.insertElementAtRear(10)
# q_linklist_obj.insertElementAtRear(20)
# q_linklist_obj.insertElementAtRear(30)
#
# q_linklist_obj.removeElementFromFront()
# q_linklist_obj.insertElementAtRear(10)
# q_linklist_obj.removeElementFromFront()
# q_linklist_obj.display()
################################################################################
class TwoDArray:


     def primenslots(self, primenumber):
         row = 10

         column =24
         #matrix = [[for i in range(row) ],[for j in range(column)]]
         matrix=[]
         rowlist=[]
         #column=[]
         k=0
         j=0

         count=0
         r = 100-1
         for i in range(row):
             rowlist.clear()

             for j in range(column):
                 if primenumber[j+k]<=r:
                     rowlist.append(primenumber[j+k])
                     count=count+1
             matrix.append(rowlist)
             k=k+count
             r = r + 100
         print(matrix)


#     row1=[]
    #     row2=[]
    #     row3=[]
    #     row4=[]
    #     row5=[]
    #     row6=[]
    #     row7=[]
    #     row8=[]
    #     row9=[]
    #     row10=[]
    #     matrix=[]
    #
    #     for i in range(len(primenumber)):
    #         if primenumber[i]<=100:
    #             row1.append(primenumber[i])
    #         elif primenumber[i]<=200:
    #             row2.append(primenumber[i])
    #         elif primenumber[i]<=300:
    #             row3.append(primenumber[i])
    #         elif primenumber[i]<=400:
    #             row4.append(primenumber[i])
    #         elif primenumber[i]<=500:
    #             row5.append(primenumber[i])
    #         elif primenumber[i]<=600:
    #             row6.append(primenumber[i])
    #         elif primenumber[i]<=700:
    #             row7.append(primenumber[i])
    #         elif primenumber[i]<=800:
    #             row8.append(primenumber[i])
    #         elif primenumber[i]<=900:
    #             row9.append(primenumber[i])
    #         elif primenumber[i]<=1000:
    #             row10.append(primenumber[i])
    #         else:
    #             pass
    #     matrix.append(row1)
    #     matrix.append(row2)
    #     matrix.append(row3)
    #     matrix.append(row4)
    #     matrix.append(row5)
    #     matrix.append(row6)
    #     matrix.append(row7)
    #     matrix.append(row8)
    #     matrix.append(row9)
    #     matrix.append(row10)
    #     #print(matrix)


        # print("Two D matrix of prime range 0-1000")
        # for row in matrix:
        #     for element in row:
        #         print(element,end=" ")
        #     print()





twoDarray_obj=TwoDArray()
##############################################################################
class BinarySearchTree:
    def factorial(self,no_of_nodes):
        fact=1
        for i in range(1,no_of_nodes+1):
            fact=fact*i
        return fact

    def countBinaryTree(self ,no_of_nodes):
        r1=2*no_of_nodes
        result1=self.factorial(r1)
        r2=no_of_nodes+1
        result2=self.factorial(r2)
        r3=no_of_nodes
        result3=self.factorial(r3)

        possiblebinarytrees=(result1/(result2*result3))

        print(possiblebinarytrees)

bst_obj=BinarySearchTree()

##############################################################################
















