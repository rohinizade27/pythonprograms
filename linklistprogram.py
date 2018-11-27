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

    def delete(self,index):
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
        cur_node=self.head
        if cur_node != None:
           print("link list is not Empty!!!")
        else:
            print("list is  Empty!!!")



link_list=Linkedlist()
link_list.isempty()
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.append(4)
link_list.display()
link_list.delete(1)
link_list.display()
link_list.isempty()

link_list.getindexitem(1)
