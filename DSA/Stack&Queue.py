# #Creating Stack using List without size limit

# class Stack:
#     def __init__(self) -> None:
#         self.list=[]
        
#     #ovveriding __str__ method to show stack when customStack obj is called
#     def __str__(self) -> str:
#         values=self.list.reverse()
#         values=[str(x) for x in self.list]
#         return '\n'.join(values)
        
#     #implementing isEmpty method
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
        
#     #push method
#     def push(self,val):
#         self.list.append(val)
#         return "Element has been pushed"
    
#     #pop method
#     def pop(self):
#         check=self.isEmpty()
#         if check == True:
#             print("Stack is empty")
#         else:
#             self.list.pop()
#             return "The element has been popped"
        
#     #peek method used to see last pushed element in stack
    
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.list[0]  #because reverse() reverses the original list.So the new list is [2,3,5] and to peek 2 ehich is 0th index.
    
#     #delete method
#     def delete(self):
#         self.list=[]
#         return self.list
    
    
# customStack=Stack()
# customStack.push(5)
# customStack.push(3)
# customStack.push(2)
# customStack.push(1)
# print(customStack)
# print(customStack.peek())
# print(customStack.delete())



# #creating Stack with size limit

# class Stacks:

#     def __init__(self, maxSize) -> None:
#         self.list = []
#         self.maxSize = maxSize

#     def __str__(self) -> str:
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return '\n'.join(values)

#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False

#     def push(self, value):
#         if len(self.list) >= self.maxSize:
#             return "Stack is full can't push more element."
#         else:
#             self.list.append(value)

#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty cannot pop anything!"
#         else:
#             self.list.pop()

#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         else:
#             return self.list[0]

#     def delete(self):
#         self.list = []
#         return self.list


# customStack = Stacks(3)
# customStack.push(5)
# customStack.push(3)
# customStack.push(2)
# print(customStack.push(1))
# print(customStack)



#Stack Using Linked Lists

# class Node:
    
#     def __init__(self,value=None):
#         self.value=value
#         self.next=next
        
# class linkedList:
#     def __init__(self):
#         self.head=None
        
#     def __iter__(self):
#         curNode=self.head
#         while curNode:
#             yield curNode
#             curNode=curNode.next
        
        
# class Stack:
#     def __init__(self):
#         self.linkedlist=linkedList()
        
#     def __str__(self):
#         values=[str(x.value) for x in self.linkedlist]
#         return '\n'.join(values)
        
#     def isEmpty(self):
#         if self.linkedlist.head==None:
#             return True
#         else:
#             return False
        
#     def push(self,val):
#         node=Node(val)
#         node.next=self.linkedlist.head  #inserting at the begining of linkedList.
#         self.linkedlist.head=node
        
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             nodeValue=self.linkedlist.head.value
#             self.linkedlist.head=self.linkedlist.head.next
#             return nodeValue
        
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         else:
#             return self.linkedlist.head.value
        
        
        
        
        
# customStack=Stack()
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# print(customStack.isEmpty()) #output False
# print(customStack.peek()) #output 3
 
 
 #Creating queue
 
# class Queue:
#     def __init__(self):
#         self.list=[]
        
#     def __str__(self):
#         value=[str(x) for x in self.list]
#         return ' '.join (value)
    
#     def isEmpty(self):
#         if len(self.list)==0:
#             return True
#         else:
#             return False
        
        
#     def enque(self,value):
#         self.list.append(value)
#         return "The element is inserted at the the end of queue"
    
#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty can not remove anything!"
#         else:
#             self.list.remove(self.list[0])
#             return "First element is removed"
        
        
#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         else:
#             return self.list[0]
        
#     def delete(self):
#         self.list==[]
#         return "Queue is deleted"
        
    
# customQueue=Queue()
# print(customQueue.isEmpty())
# print(customQueue.enque(4))
# print(customQueue.enque(12))
# print(customQueue.enque(7))
# print(customQueue)
# print(customQueue.dequeue())
# print(customQueue)

#Circular Queue
# class Queue:
    
#     def __init__(self,maxSize):
#         self.item = [None]*maxSize
#         self.maxSize=maxSize
#         self.top = -1
#         self.start = -1
        
#     def __str__(self):
#         values=[str(x) for x in self.item]
#         return ' '.join(values)
    
#     def isFull(self):
#         if self.top+1==self.start:
#             return True
#         elif self.start == 0 and self.top == self.maxSize - 1:
#             return True
#         else:
#             return False
        
#     def isEmpty(self):
#         if self.top == -1:
#             return True
#         else:
#             return False
        
#     def enqueue(self,value):
#         if self.isFull():
#             return "Queue is full!, cannot insert element"
#         else:
#             if self.start == -1:
#                 self.start = 0
#                 self.top = (self.top+1) % self.maxSize
#                 self.item[self.start] = value
#                 return "value inserted"
#             else:
#                 self.top = (self.top+1) % self.maxSize
#                 self.item[self.top] = value
#                 return "value inserted"
    
#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"
                
#         elif (self.start == self.top): #checking if there is only one element in queue
#             firstelement=self.item[self.start]
#             # start=self.start
#             self.start = -1
#             self.top = -1
            
#         else:
#             firstelement=self.item[self.start]
#             self.item[self.start]=None #Atfter removing first element set it to None
#             self.start = (self.start + 1)% self.maxSize
        
#         return firstelement
    
#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty!!"
            
#         return self.item[self.start]
    
#     def deleteQueue(self):
#         self.item = self.maxSize * [None]
#         self.start=-1
#         self.top=-1
    
        

# customeQueue=Queue(5)
# customeQueue.enqueue(20)       
# customeQueue.enqueue(12)       
# customeQueue.enqueue(34)
# customeQueue.enqueue(54)
# customeQueue.enqueue(23)
# print(customeQueue.dequeue())
# print(customeQueue.dequeue())
# customeQueue.enqueue(100)
# print(customeQueue.peek())
# print(customeQueue)


#Queue using Linked Lists




    
        