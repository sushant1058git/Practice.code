'''Doubly Linked List'''

class Node:
    def __init__(self,val,nextNode=None,prevNode=None):
        self.val=val
        self.nextNode=nextNode
        self.prevNode=prevNode
        

class DLL:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
        
    def insertFirst(self,newValue):
        newNode=Node(newValue)
        if self.head is None:
            self.head=newNode
            if self.tail is None:
                self.tail=self.head
        else:
            newNode.nextNode=self.head
            newNode.prevNode=None
            if self.head is not None:  #to avoid null pointer error because head may be none while inseting first time
                self.head.prevNode=newNode
            self.head=newNode
            
    def InserLast(self,newValue):
        newNode=Node(newValue)
        if self.tail is None:
            d.insertFirst(newValue)
            return
        else:
            newNode.prevNode=self.tail
            newNode.nextNode=None
            if self.tail is not None:
                self.tail.nextNode=newNode #to avoid null pointer error because head may be none while inseting first time
            self.tail=newNode
        
        
        
    def insertAtIndex(self,value,index):
        newNode=Node(value)
        if index==0:
            d.insertFirst(value)
        temp=self.head
        for i in range(1,index):
            temp=temp.nextNode
        newNode.nextNode=temp.nextNode
        newNode.prevNode=temp
        temp.nextNode.prevNode=newNode
        temp.nextNode=newNode
        
            
    def displayDLL(self):
        tempNode=self.head
        last=None
        while tempNode is not None:
            print(tempNode.val,'->',end="")
            last=tempNode
            tempNode=tempNode.nextNode
        print("END")
        
        # print("Reversed Linked List : ")
        # while last is not None:
        #     print(last.val,'-> ',end="")
        #     last=last.prevNode
        # print("START")
        
        
d=DLL()
d.insertFirst(5)
d.insertFirst(12)
d.insertFirst(16)
d.insertFirst(51)
d.insertFirst(78)
d.insertFirst(54)
d.InserLast(100)
d.insertAtIndex(17,3)
d.displayDLL()