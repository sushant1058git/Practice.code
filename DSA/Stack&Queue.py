#Creating Stack using List without size limit

class Stack:
    def __init__(self) -> None:
        self.list=[]
        
    #ovveriding __str__ method to show stack when customStack obj is called
    def __str__(self) -> str:
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
        
    #implementing isEmpty method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    #push method
    def push(self,val):
        self.list.append(val)
        return "Element has been pushed"
    
    #pop method
    def pop(self):
        check=self.isEmpty()
        if check == True:
            print("Stack is empty")
        else:
            self.list.pop()
            return "The element has been popped"
        
    #peek method used to see last pushed element in stack
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[0]  #because reverse() reverses the original list.So the new list is [2,3,5] and to peek 2 ehich is 0th index.
    
    #delete method
    def delete(self):
        self.list=[]
        return self.list
    
    
customStack=Stack()
customStack.push(5)
customStack.push(3)
customStack.push(2)
customStack.push(1)
print(customStack)
print(customStack.peek())
print(customStack.delete())
