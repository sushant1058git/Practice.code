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
            self.tail=self.head
            newNode.next=self.head
            self.head=newNode
            
    def printLL(self):
        tempNode=self.head
        while tempNode is not None:
            print(str(tempNode.val)+'-->',end="")
            tempNode=tempNode.next
        print("END")
            
newLL=LinkedList()
print(newLL.isEmpty())
newLL.insertFirst(45)
newLL.insertFirst(454)
newLL.insertFirst(495)
newLL.printLL()
print(newLL.isEmpty())

