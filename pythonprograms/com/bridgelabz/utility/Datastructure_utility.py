from datetime import date, timedelta
class Node:
    def __init__(self, data=None):
        """
        This method is to initialize node object
        :param data: value given to node
        """
        self.data = data #Assign data
        self.next = None #make next of node is none


class Linkedlist:
    def __init__(self):
        """
        This method is to initialize head
        """
        self.head = Node()

    def append(self, data):
        """
        This function is to insert a new node after the previous node
        :param data:Is the data which you want to insert
        """
        new_node = Node(data)#create new node and assign data to it
        traverse_node = self.head
        while traverse_node.next != None:#traverse till end of linked list
            traverse_node = traverse_node.next
        traverse_node.next = new_node#make the last node new node

    def length(self):
        """
        This function is to find the length of linked list
        :return: It returns the total length
        """
        traverse_node = self.head
        total = 0
        while traverse_node.next != None:#travese till end of the of the linked list
            total += 1
            traverse_node = traverse_node.next#goto to next node
        return total

    def display(self):
        """
         This method is to display linked list
        """
        elements = []#list to store linked list data
        traverse_node = self.head
        while traverse_node.next != None:#travese till end of the list
            traverse_node = traverse_node.next
            elements.append(traverse_node.data)#append each data to list
        print(elements)#display list

    def getindexitem(self, index):
        """
        :param index:Is the index of which data you want
        :return:data on given index
        """
        if index >= self.length():
            print("index out of range")
            return None

        cur_index = 0
        traverse_node = self.head
        while traverse_node.next != None: #traverse till end of the list
            traverse_node = traverse_node.next
            if cur_index == index: #check current index is the index you want
                print("Element at", index, "index is:", traverse_node.data)
                return traverse_node #return current node
            cur_index += 1

    def remove(self, index):
        """
        This method is to delete the data from specified index
        :param index: It is the index of node you want to delete
        :return:It return data on given index
        """
        if index >= self.length():
            print("index out of range")
            return
        cur_index = 0
        cur_node = self.head
        while cur_node.next != None:#traverse till end of
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1

    def isempty(self):
        """
         This function is to check linked list is empty or not
        """
        traverse = self.head

        if traverse.next == None:
            print("link list Empty!!!")
        else:
            print("list is not Empty!!!")

    def additematfront(self, data):
        """
         This function is to insert the node at front of linked list
        :param data: is the data user want to insert
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def searchElement(self, key):
        """
        This function is to search element from linked list
        :param key: is the data user wants to search
        :return: true if  data is present else return false
        """
        traverse_pointer = self.head
        while traverse_pointer.next != None:
            # print(key)
            # print(traverse_pointer.data)
            if traverse_pointer.data == key:
                return True
            traverse_pointer = traverse_pointer.next
            # print(traverse_pointer.data)
        if traverse_pointer.data == key:
            return True
        return False

    def pop(self, data):
        """
         This function is to delete the specified node
        :param data: is the node user want to delete
        :return:specified deleted node
        """
        cur_node = self.head
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data == data:
                last_node.next = cur_node.next
                return
        return

    def searchFromFile(self):
        """
        This function read the data from file and store it on linked list.
        user will enter the element to search if it is present in linked list
        then that element is poped from list else element is added on list

        """
        fileobject = open("inputword.txt", "w+")#create file object for read write operation
        list = ["rohini ","reshma", "rajat ", "sai ", "akansha"]
        fileobject.writelines(list)#write data on file
        fileobject.close()#close file

        fileojbect = open("inputword.txt", "r")#open file for reading data

        storefilecontent = fileojbect.read()
        storefilecontent = str(storefilecontent).split()
        # print(storefilecontent)
        fileojbect.close()

        for i in range(len(list)):
            link_list.append(list[i])

        link_list.display()

        key = input("Enter the Element you want to search:")
        result = link_list.searchElement(key)
        print(result)

        if result == False:
            link_list.append(key)
        else:
            link_list.pop(key)

        link_list.display()


link_list = Linkedlist()


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


# link_list.display()


# link_list.getindexitem(1)


###########################################################################################

class OrderedLinkList:
    def __init__(self):
        self.head = None

    def insertdata(self, data):
        """
        This function is to insert the data on sorted way
        :param data: is the data user wants to insert
        """
        new_node = Node(data)

        # if head is null them
        if self.head is None:
            new_node.next = self.head
            self.head = new_node


        # if head data is greater than new node data
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node # new node will become head

        else:


            traverse_node = self.head
            # insert the new node after previous node if data of previous
            # node less than new node
            if traverse_node.next.data < new_node.data:
                # and traverse_node.next.data < new_node.data:
                while traverse_node.next != None :
                    traverse_node = traverse_node.next

                new_node.next = traverse_node.next
                traverse_node.next = new_node

            elif traverse_node.next.data > new_node.data:
                # and traverse_node.next.data > new_node.data:
                while traverse_node.next != None:
                    traverse_node = traverse_node.next
                new_node.next = self.head
                self.head=new_node


    def insertatfront(self, data):
        """
            This method is to display linked list
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def searchElement(self, key):
        """
        This function is to search element from linked list
        :param key: is the data user wants to search
        :return: true if  data is present else return false
        """
        traverse_pointer = self.head
        while traverse_pointer.next != None:

            if traverse_pointer.data == key:
                return True
            traverse_pointer = traverse_pointer.next

        if traverse_pointer.data == key:
            return True
        return False


    def display(self):
        elements = []
        traverse_node = self.head
        while traverse_node.next != None:
            traverse_node = traverse_node.next
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

        self.stack = list()

    def push(self, data):
        """
        This function is to push element on stack
        :param data: is the data user want to insert
        """
        if len(self.stack) > self.stackMaxsize:#check for overflow condtion of stack
            print("Overflow!!! no enough space ")
        else:
            tp = self.top
            tp += 1 #increment top
            self.stack.insert(tp, data) #insert data on top
            # self.stack[tp]=data

    def pop(self):
        """
        This function is to pop data from stack
        :return: topmost element on stack
        """
        if self.stack == []:#check if stack is empty
            print("Underflow!!! no items in stack")
        else:              #else pop the topmost element from stack
            tp = self.top
            temp = self.stack[tp]
            self.stack.pop()
            tp -= 1
            return temp

    def isempty(self):
        """
         This function is to check stack is empty or not
        :return: true if stack is empty else return false
        """
        if self.stack == []:
            return True

    def display(self):
        print(self.stack)

    def checkblanceparantheses(self):
        """
         Thisfunction is to check the given expression is having balance
         parantheses or not
        """
        expression = input("Enter the Expression:")
        balance = True
        for i in range(len(expression)):
            if expression[i] == '(': #push every occurance of '(' on stack
                stack_obj.push(i)

            else:
                if stack_obj.isempty():
                    balance = False
                else:
                    if expression[i] == ')':#pop from stack when there occurance of ')'
                        stack_obj.pop()

        result = stack_obj.isempty()

        if result == True and balance == True:
            print("Expression is blanced..!!!")
        else:
            print("expression is not balanced..!!")


stack_obj=Stack()
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


##########################################################################################
class Queue:
    def __init__(self):
        self.queue = list()

    def insertElement(self, data, maxlen):
        """
        This function is to insert the element on queue
        :param data: is the data,user wants to insert
        :param maxlen: maximum length of queue
        """
        rear = len(self.queue)
        rear = rear + 1

        # print(rear)
        if rear > maxlen:#check if there is enough space on stack for insertin element
            print("Overflow!!..no enough space..!!")
            exit()
        else:
            self.queue.append(data)#insert the data at the rear

    def deleteElement(self):
        """
            This function is to delete the data of queue from front
        """
        if queue_obj.isEmpty():#check if queue is empty or not
            print("Underflow!!..No Elements on stack!!")
            exit()
        else:
            self.queue.pop(0)#delete data

    def isEmpty(self):
        """
         This function is to check queue is empty or not
        :return: true if it is empty else return false
        """
        if self.queue == []:
            return True

    def display(self):
        print(self.queue)

    def withdraw(self, available_balance):
        """
         This function is to withdraw the amount from bank balance
        :param available_balance: is total available balance of bank
        """
        withdraw_cash = int(input("please Enter the withdraw amount:"))
        if available_balance >= withdraw_cash:#withdraw amount should be greater than available balance
            available_balance -= withdraw_cash
            print("Available Balance:", available_balance)
            print("Withdraw Amount:", withdraw_cash)
            queue_obj.deleteElement()
            # queue_obj.display()

        else:
            print("SORRY !!! Insufficient Balance..!!")
            queue_obj.deleteElement()
            # queue_obj.display()

    def deposit(self, available_balance):
        """
         This function is to deposit amount to available balance of bank
        :param available_balance: total available balance of bank
        """
        deposit_cash = int(input("Enter the deposit amount:"))
        available_balance += deposit_cash
        print("Available Balance:", available_balance)
        print("Withdraw Amount:", deposit_cash)
        queue_obj.deleteElement()
        queue_obj.display()

    def cashCounterLogic(self):
        """
          This function simulate the cash counter of bank.
          there is queue of people ,every people have two choices 1.withdraw and 2.deposit
          if user choose 1st then withdraw function will be called if user choose 2nd then deposite
          function will be called

        """
        available_balance = 500000
        print("Available Bank Balance = 500000")
        maxlen = int(input("How may persons are there in a Queue?"))
        print("people in queue:")
        for i in range(maxlen):
            person_id = input("please enter the id of person:")
            queue_obj.insertElement(person_id, maxlen)

        for i in range(maxlen):
            queue_obj.display()
            print("___You have two choices___")
            print("1. withdraw Cash")
            print("2. Deposit cash")
            ch = int(input("Enter your choice:"))
            if ch == 1:
                queue_obj.withdraw(available_balance)
            elif ch == 2:
                queue_obj.deposit(available_balance)
            else:
                print("!!..Invalid choice..!!")


queue_obj = Queue()


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


###########################################################################################
class checkpalindrome:
    def __init__(self):
        pass

    def palindromeLogic(self, string):
        """
         This function is to check given string is palindrome or not
        :param string:user entered string
        """
        stringlist = []
        for i in range(len(string)):
            stringlist.append(string[i])

        for i in range(len(string)):
            dequeue_obj.insertElementAtRear(string[i], len(string))#insert the string element on queue

        storelement = dequeue_obj.dequeue

        reverselist = []
        for j in range(len(storelement)):
            element = dequeue_obj.deleteElementfromRear()#delete string elements from queue
            # print(element)
            reverselist.append(element)
        print("original string:", stringlist)
        print("reverse string:", reverselist)
        if stringlist == reverselist: # compare both the string
            print("string is palindrome")
        else:
            print("string is not palindrome")


#############################################################################
class Dequeue:
    def __init__(self):
        self.dequeue = list()

    def insertElementAtRear(self, data, maxlen):
        """
          This function is to insert the element to queque at rear
        :param data: is the data user wants to insert
        :param maxlen: maximum length of queue
        """
        rear = len(self.dequeue)
        rear = rear + 1

        # print(rear)
        if rear > maxlen:
            print("Overflow!!..no enough space..!!")
            exit()
        else:
            self.dequeue.append(data)

    def insertElementAtFront(self, data, maxlen):
        """
         This function is to insert the data at the front of queue
        :param data: is the data user wants to insert
        :param maxlen: maximum length of queue
        """
        rear = len(self.dequeue)
        rear = rear + 1

        if rear > maxlen:
            print("Overflow!!..no enough space..!!")
            exit()
        else:
            self.dequeue.insert(0, data)

    def deleteElementfromfront(self):
        """
          This function is to delete data of queue from front
        """
        if dequeue_obj.isEmpty():
            print("Underflow!!..No Elements on stack!!")
            exit()
        else:
            self.dequeue.pop(0)

    def deleteElementfromRear(self):
        """
         This function is to delete data of queue from rear
        :return: it returns deleted data from queue
        """
        rear = len(self.dequeue)
        rear = rear - 1
        # print(rear)
        if dequeue_obj.isEmpty():
            print("Underflow!!..No Elements on stack!!")
            exit()
        else:
            return self.dequeue.pop(rear)

    def isEmpty(self):
        """
        check if string is empty or not
        :return: true if it is empty, else return false
        """
        if self.dequeue == []:
            return True

    def display(self):
        """
         This function is to display content of queue
        """
        print(self.dequeue)


# maxlen=5
dequeue_obj=Dequeue()
# dequeue_obj.insertElementAtRear(10,maxlen)
# dequeue_obj.insertElementAtRear(11,maxlen)
# dequeue_obj.insertElementAtFront(21,maxlen)
# dequeue_obj.insertElementAtFront(26,maxlen)
# dequeue_obj.deleteElementfromfront()
# dequeue_obj.deleteElementfromRear()
# dequeue_obj.insertElementAtFront(28,maxlen)
# dequeue_obj.deleteElementfromRear()
# dequeue_obj=Dequeue()

##############################################################################
class Anagram:

    def anagramLogic(self,primenumber,anagramlist):
        """
         This function is to find whether given to strings are anagram to each other or not
        :param string1: 1st string to check for anagram
        :param string2: 2nd string to check for anagram
        :param anagramlist: list to store anagram strings
        :return:list of string which are angram

        """

        for i in range(len(primenumber)):
            for j in range(len(primenumber)):
                if primenumber[i] > 0 and primenumber[j] > 0:
                    string1 = str(primenumber[i])
                    string2 = str(primenumber[j])

                    # the sorted strings are checked
                    if string1 != string2:
                        if (sorted(string1) == sorted(string2)):
                            anagramlist.append(string1)
                            anagramlist.append(string2)

        #print(anagramlist)
        return anagramlist


    def unique_list(self, storeanagram):
        uniq_list = []
        uniq_set = set()
        for item in storeanagram:
            if item not in uniq_set:
                uniq_list.append(item)
                uniq_set.add(item)
        return uniq_list

    def stackOperationOnAnagramlist(self, uniquelist):
        """
        This function is to push all the anagram strings(prime nos) on stack
        :param uniquelist: returns all the poped anagram from stack
        """
        popedElement = []
        print("Anagram number after pushed it into stack...")
        for i in range(len(uniquelist)):
            stackllist.push(uniquelist[i])#push on stack
        stackllist.display()

        print("Anagram number after poped it from stack...")
        for i in range(len(uniquelist)):
            item = stackllist.pop()#pop from stack
            popedElement.append(item)
        # stackllist.display()
        print(popedElement)

    def QueueOperationOnAnagramlist(self, uniquelist):
        """
         This function is to insert all the anagram strings(prime nos) on queue
        :param uniquelist: eturns all the deleted anagram strings from queue
        """
        deletedElement = []
        print("Anagram number after inserted into queue...")
        for i in range(len(uniquelist)):
            q_linklist_obj.insertElementAtRear(uniquelist[i])#insert element at rear
        q_linklist_obj.display()

        print("Anagram number after deleted from queue...")
        for i in range(len(uniquelist) + 1):
            item = q_linklist_obj.removeElementFromFront()#delete element from front
            deletedElement.append(item)
        # stackllist.display()
        print(deletedElement)


###################################################################################
class StackByLink:

    def __init__(self):
        """
        Initialized frist node as head
        """
        self.head = Node()

    def push(self, data):
        """
         This function is to push the element on stack
        :param data: is the data user wants to push on to stack
        """
        new_node = Node(data)
        traverse = self.head
        while traverse.next != None:#traverse till it find last node
            traverse = traverse.next
        traverse.next = new_node#next of last node is newnode

    def display(self):
        """
        This is to display the stack element
        """
        elements = []
        traverse = self.head
        while traverse.next != None:#traverse till it find last node
            traverse = traverse.next
            elements.append(traverse.data)
        print(elements)

    def pop(self):
        """
        This function is to pop data fron stack
        :return:it returns deleted data
        """
        traverse = self.head

        if traverse.next == None:#check if stack is empty or not
            print("Underflow..!!")

        while traverse.next != None:#traverse till it find last node
            t = traverse.next
            if t.next == None:#check if previous node's next is null
                traverse.next = None
                return t.data
            traverse = traverse.next

    def isUnderflow(self):
        """
         This function is to check whether stack is empty or not
        :return:
        """
        traverse = self.head
        if traverse.next == None:
            return True
        else:
            return False


stackllist = StackByLink()


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
        self.head = Node()

    def insertElementAtRear(self, data):
        """
         This function is to inert element on queque at rear
        :param data: is the data which user wants to add
        """
        new_node = Node(data)
        traverse = self.head
        while traverse.next != None:#traverse it you find last node
            traverse = traverse.next
        traverse.next = new_node

    def removeElementFromFront(self):
        """
         This function is to remove the elements of queue from front
        :return: it returns deleted node
        """
        if self.head is None:#if liked list doen't have element
            return None

        else:
            pop_node = self.head.data#store the front node on pop_node
            self.head = self.head.next#make next of front node as head
            return pop_node

    def display(self):
        """
         This function is to display the queue elements
        """
        elements = []
        traverse = self.head
        while traverse.next != None:#traverse till it find last node
            traverse = traverse.next
            elements.append(traverse.data)
        print(elements)


q_linklist_obj = QueeByLinklist()


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
        """
        This function is to print the prime number from range 0-1000 in 2D matrix format
        :param primenumber: list of prime number
        """
        row = 10
        column = 24
        # list of list to store prime number in slots of 100
        matrix = [[0 for j in range(column)] for i in range(row)]

        rowlist = []
        k = 0
        j = 0

        count = 0
        r = 100
        for i in range(row):
            # rowlist.clear()

            for j in range(column):

                if k < len(primenumber):
                    # to create slots of prime between 100,200 so on
                    if primenumber[k] <= r:
                        matrix[i][j]=primenumber[k]
                        k = k + 1
                    # count=count+1
            # k=k+1
            # newlist=rowlist
            # matrix.append(newlist)
            # k=k+count
            r = r + 100
        #print(matrix)

        print("Two D matrix of prime range 0-1000")
        for row in matrix:
            for element in row:
                if element!=0:
                    # print prime numbers in matrix format
                    print(element, end=" ")
            print()
twoDarray_obj = TwoDArray()


##############################################################################
class BinarySearchTree:
    def factorial(self, no_of_nodes):
        """
        This function is to find factorial of given number
        :param no_of_nodes: number of which user want to find factorial
        :return: terurns the factorial value
        """
        fact = 1
        for i in range(1, no_of_nodes + 1):
            fact = fact * i
        return fact

    def countBinaryTree(self, no_of_nodes):
        """
        This function is to find the number of possible binary trees of given number of nodes
        :param no_of_nodes: given number of nodes
        """
        r1 = 2 * no_of_nodes
        result1 = self.factorial(r1)
        r2 = no_of_nodes + 1
        result2 = self.factorial(r2)
        r3 = no_of_nodes
        result3 = self.factorial(r3)

        possiblebinarytrees = (result1 / (result2 * result3))

        print("possible binary trees are:",possiblebinarytrees)


bst_obj = BinarySearchTree()

##############################################################################
class HashFunction:
    def hashFunctionLogic(self, no_of_slots,storeelement):
        """
        This function is to store the given number in hashtable
        :param no_of_slots: total number of slots in hashtable
        :param storeelement: list of element to store on hashtable
        :return: it returns hastlist
        """
        #element=[54, 26, 93, 17, 77, 31]

        hashlist=[None]*no_of_slots
        # hashlist.pop(4)
        # hashlist.insert(4,26)
        # hashlist.insert(2,45)
        #print(hashlist)
        value=no_of_slots+1
        for i in range(len(storeelement)):
                position=storeelement[i]%value

                if hashlist[position]==None and position<len(hashlist):
                    hashlist.pop(position)
                    hashlist.insert(position,storeelement[i])

                else:
                    k = 0
                    while k<len(hashlist):
                        k = k + 1
                        if (position+k)<len(hashlist) or position-k >0:
                            if hashlist[position+k]==None:
                                hashlist.pop(position+k)
                                hashlist.insert(position, storeelement[i])
                                break
                            elif hashlist[position-k]==None:
                                hashlist.pop(position - k)
                                hashlist.insert(position, storeelement[i])
                                break

        #print(hashlist)
        return hashlist



    def hashSearchFunction(self,key,hashlist,no_of_slots):
        """
         This function is to search the element on hash table
        :param key: data you wants to search
        :param hashlist: the hashtable on which elements are stored
        :param no_of_slots: number of slots in hash table
        """
        value = no_of_slots + 1

        for i in range(len(hashlist)):
                position=key%value #find the index from given data

                if hashlist[position]==key and position<len(hashlist):#check if data is presnt on that index postion
                    print("key is present at",position,"index")
                    exit()

                else:
                    k = 0
                    while k<len(hashlist):
                        k = k + 1
                        if (position+k)<len(hashlist) or position-k >0:#check data on next index
                            if hashlist[position+k]==key:
                                print("key is present at", position+k, "index")
                                exit()
                            elif hashlist[position-k]==key: # check data on previous index
                                print("key is present at", position-k, "index")
                                exit()

hashfunction_object=HashFunction()

#########################################################################################
class Calendar:

    def get_first_day(self,year,month,d_years=0, d_months=0):
        """
        This function is to find first day of month
        :param year: user entered year
        :param month: user enterd month
        :param d_years: it is 0 at initial state
        :param d_months: it is 0 at initial state
        :return: it returns 1st day of month
        """

        y = year + d_years
        m = month + d_months
        a, m = divmod(m - 1, 12)
        return date(y + a, m + 1, 1)

    def leapyear(self,year):
        """
         This function is to find given year is leap year or not
        :param year:given year
        :return:return True if year is leap year else return False
        """
        if (int(year) % 400 == 0) and (int(year) % 100 == 0) or (int(year) % 4 == 0):
            return True
        else:
            return False

    def calanderlogic(self,firstday_of_month,month,year):
        """
         This function is to create calculator of given month and year
        :param firstday_of_month: starting day of month
        :param month: given month to create calender
        :param year: given year to create calender
        """
        if month<=12:
            print("firstday_of_month:", firstday_of_month)
            totalmonthday = 0
            if month == 2:
                # check given year is leap year or not
                isleapyear = calendar_obj.leapyear(year)
                if isleapyear == True:
                    totalmonthday = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                     24, 25, 26, 27, 28, 29]
                else:
                    totalmonthday = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                     24, 25, 26, 27, 28]

            elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                totalmonthday = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                 25, 26, 27, 28, 29, 30, 31]
            else:
                totalmonthday = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                 25, 26, 27, 28, 29, 30]

            for a in range(firstday_of_month):
                for d in range(firstday_of_month):
                    totalmonthday.append(len(totalmonthday) + d)
                    break

            row = 7
            column = 7
            k = 0
            matrix = [[0 for j in range(column)] for i in range(row)]
            for i in range(row):

                for j in range(column):
                    if k < len(totalmonthday):
                        # for printing first day on proper position
                        if j >= firstday_of_month:
                            # for storing element on first row
                            matrix[i][j] = totalmonthday[k - firstday_of_month]
                    if k < len(totalmonthday):
                        if i > 0:
                            # for storing elements on 2nd row onwards
                            matrix[i][j] = totalmonthday[k - firstday_of_month]

                    k = k + 1

            # printing the matrix in 2D format
            print("**********************************")
            print("Calender of month:", month, "year:", year)
            print("**********************************")
            print("Su  Mo  Tu  We  Th  Fr  Sat")
            for row in matrix:
                for element in row:

                    if element == 0:
                        print("  ", end="  ")
                    else:
                        if element <= 9:
                            print(element, end="   ")
                        else:
                            print(element, end="  ")
                print()
        else:
            print("Invalid input..!!!")


calendar_obj = Calendar()


















#######################################################################################3






