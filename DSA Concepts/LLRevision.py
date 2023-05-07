class Node:
    def __init__(self,val,next=None) -> None:
        self.val=val
        self.next=next
        
        
        
class LinkedList:
    def __init__(self,head=None,tail=None) -> None:
        self.head=head
        self.tail=tail
        
    # def __str__(self) -> str:
    #     while self.head is not None:
    #         print(self.head)
    #         self.head=self.head.next
    #         return str(self.head)
    
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
        
    def insertFirst(self,value):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
            
    def printLL(self):
        tempNode=self.head
        while tempNode is not None:
            print(str(tempNode.val)+'-->',end="")
            tempNode=tempNode.next
        print("END")
        
    def insertLastUsingTail(self,value):
        newNode=Node(value)
        if self.tail == None:
            self.tail=newNode
            self.head=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        
    def deleteFirst(self):
        self.head=self.head.next
        
    def deleteLast(self):
        tempNode=self.head
        while tempNode.next != self.tail:
            tempNode=tempNode.next
        self.tail=tempNode
        self.tail.next=None
            
    
            
newLL=LinkedList()
print(newLL.isEmpty())
newLL.insertFirst(45)
newLL.insertFirst(454)
newLL.insertFirst(495)
newLL.printLL()
newLL.insertLastUsingTail(100)
newLL.insertLastUsingTail(300)
newLL.printLL()
print("LL after deleting first element..")
newLL.deleteFirst()
newLL.printLL()
print("LL after deleting last element..")
newLL.deleteLast()
newLL.printLL()

