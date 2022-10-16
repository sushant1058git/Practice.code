#Create linked list 3-->5-->7
'''Without using oops, it is just a simple linked list without insert function'''

# class LinkedListNode:
#     def __init__(self,value,next_node=None):
#         self.value=value
#         self.next_node=next_node
        
# #creating nodes      
# n1=LinkedListNode('3')
# n2=LinkedListNode('5')
# n3=LinkedListNode('7')

# #creating links
# n1.next_node=n2     #n1-->n2
# n2.next_node=n3     #n2-->n3

# #n1-->n2-->n3

# current_node=n1   #setting n1 as current node

# while True:
#     print(current_node.value + " -->",end=' ')
#     if current_node.next_node is None:
#         print("None")
#         break
#     current_node=current_node.next_node



'''Now we create Linked list using Oops with an insert function'''

# from hashlib import new
# from operator import ne


# class LinkedListNode:
#     def __init__(self,value,next_node=None):
#         self.value=value
#         self.next_node=next_node
        
# class LinkedList():
#     def __init__(self,head=None):
#         self.head=head
#         print("called const")
    
#     def insert(self,value):
#         node=LinkedListNode(value)
#         if self.head==None:
#             self.head=node
#             return
#         else:
#             current_node=self.head
            
#         while True:
#             if current_node.next_node is None:
#                 current_node.next_node=node
#                 break
#             current_node=current_node.next_node
            
#     def printLinkedList(self):
#         current_node=self.head
#         print(type(current_node))
#         while current_node is not None:
#             print(str(current_node.value) + '-->', end='')
#             current_node=current_node.next_node
#         print("None")
            

# l1=LinkedList()
# l1.printLinkedList()
# l1.insert(3)
# l1.printLinkedList()
# l1.insert(4)
# l1.printLinkedList()
# l1.insert(5)
# l1.printLinkedList()



# class Node:
#     def __init__(self,value,nextNode=None):
#         self.value=value
#         self.nextNode=nextNode
        
        

# class LinkedList:
#     def __init__(self,head=None):
#         self.head=head
        
#     def insert(self,element):
#         newNode=Node(element)
#         if self.head is None:
#             self.head=newNode
#             return
#         else:
#             current_element=self.head
        
#         while True:
#             if current_element.nextNode is None:
#                 current_element.nextNode=newNode
#                 break
#             else:
#                 current_element=current_element.nextNode
                
                
#     def printLinkedList(self):
#         current_node=self.head
#         print(type(current_node))
#         while current_node is not None:
#             print(str(current_node.value) + '-->', end='')
#             current_node=current_node.nextNode
#         print("None")
        
        
# l1=LinkedList()
# l1.printLinkedList()
# l1.insert(3)
# l1.printLinkedList()
# l1.insert(4)
# l1.printLinkedList()
# l1.insert(5)
# l1.printLinkedList()




class Node:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode
        
        
class LinkedList:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
        

    def insertFirst(self,element):  #insert element at first position (Head keeps changing)
        newNode=Node(element)
        if self.head is None:
            self.head=newNode
            if self.tail is None:   #Adding first item
                self.tail=self.head
        else:
            newNode.nextNode=self.head
            self.head=newNode
            
    def insertLast(self,element):   #insert element at last position (Head is fixed)
        newNode=Node(element)
        if self.head is None:
            self.head=newNode
            return
        else:
            current_node=self.head  #always points to 3 i.e; head
            # print(current_node)
            
        while True:
            if current_node.nextNode is None:
                current_node.nextNode=newNode
                break
            else:
                current_node=current_node.nextNode
                
    def inserLastUsingTail(self,element):
        newNode=Node(element)
        if self.tail is None:
            l1.insertFirst(element)
            return
        else:
            self.tail.nextNode=newNode
            self.tail=newNode
            
    def insert(self,val,index):
            temp=self.head  
            for i in range(1,index):
                temp=temp.nextNode 
            newNode=Node(val)
            newNode.nextNode=temp.nextNode
            temp.nextNode=newNode
            
    def deleteFirst(self):
        self.head=self.head.nextNode
        
    def countIndexValue(self):
        temp=self.head
        index=0
        while temp.nextNode is not None:
            temp=temp.nextNode
            index +=1
        return index
            
        
    def deleteLast(self):
        temp=self.head
        index=l1.countIndexValue()
        for i in range(1,index-1):
            temp=temp.nextNode
        self.tail=temp.nextNode
        self.tail.nextNode=None               
            
    def delete(self,index):
        temp=self.head
        for i in range(1,index):
            temp=temp.nextNode
        temp.nextNode=temp.nextNode.nextNode
        

    def printLinkedList(self):
        tempNode=self.head
        while tempNode is not None:
            print(tempNode.value,'-->',end=' ')
            tempNode=tempNode.nextNode
        print("END")
        
        
        
        
# l1=LinkedList()
# l1.printLinkedList()
# l1.insertFirst(3)
# l1.printLinkedList()
# l1.insertFirst(4)
# l1.printLinkedList()
# l1.insertFirst(5)
# l1.printLinkedList()

l1=LinkedList()
l1.printLinkedList()
l1.insertFirst(3)
l1.printLinkedList()
l1.insertFirst(4)
l1.printLinkedList()
l1.inserLastUsingTail(5)
l1.printLinkedList()
l1.inserLastUsingTail(7)
l1.printLinkedList()
l1.inserLastUsingTail(9)
l1.printLinkedList()
l1.inserLastUsingTail(11)
l1.printLinkedList()
l1.inserLastUsingTail(45)
l1.printLinkedList()
l1.inserLastUsingTail(43)
l1.printLinkedList()
l1.inserLastUsingTail(41)
l1.printLinkedList()
l1.insert(11,3)
l1.printLinkedList()
# l1.deleteFirst()
# l1.printLinkedList()
l1.deleteLast()
l1.printLinkedList()
# l1.countIndexValue()
l1.delete(3)
l1.printLinkedList()




