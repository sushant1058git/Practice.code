# # Python program to demonstrate in-built poly-morphic functions
	
# # len() being used for a string
# print(len("geeks"))
	
# # len() being used for a list
# print(len([10, 20, 30]))


# # A simple Python function to demonstrate
# # Polymorphism

# def add(x, y, z = 0):
# 	return x + y+z

# # Driver code
# print(add(2, 3))
# print(add(2, 3, 4))


# class Bird:
#     def __init__(self,name):
#         self.name=name
#         print(f"{self.name} is flying ")



# obj=Bird("uno")
# print(type(obj))

# class Duck:
    
#     def quack(self):
#         print("quack quack")
    
#     def fly(self):
#         print("Flap flap")
        
# class Person:
#     def quack(self):
#         print("i'm quacking like a duck")
        
#     def fly(self):
#         print("I'm flapping like a duck")
        
# def quack_and_fly(thing):
#      #Not Duck-typed (Non-pythonic)
#     if isinstance(thing,Duck):    #Checking if thing is a intance of Duck
#          thing.quack()
#          thing.fly()
    
#     else:
#         print("This has to be a duck")
        
# d=Duck()
# quack_and_fly(d)

# p=Person()
# quack_and_fly(p)


'''If attr is not present it will throw attr error'''


# class Duck:
    
#     def quack(self):
#         print("quack quack")
    
#     def fly(self):
#         print("Flap flap")
        
# class Person:
#     def quack(self):
#         print("i'm quacking like a duck")
        
        
# def quack_and_fly(thing):
#          thing.quack()
#          thing.fly()
    
        
# d=Duck()
# quack_and_fly(d)

# p=Person()
# quack_and_fly(p)



# '''Using hasattr to check if required attr is present in the class or not'''

# class Duck:
    
#     def quack(self):
#         print("quack quack")
    
#     def fly(self):
#         print("Flap flap")
        
# class Person:
#     def quack(self):
#         print("i'm quacking like a duck")

        
# def quack_and_fly(thing):
#     if hasattr(thing,'quack'):
#          thing.quack()
#     if hasattr(thing,'fly'):
#          thing.fly()
    
        
# d=Duck()
# quack_and_fly(d)
# p=Person()
# quack_and_fly(p)
    


# '''Method Overloading'''

# class Operator_overloading:
#     def __init__(self,a):
#         self.a=a
    
    
# obj1=Operator_overloading(1)
# obj2=Operator_overloading(2)

# print(obj1+obj2)    


'''Error rectification using magic method'''

class operator_overloading:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,o):
        return self.a+o.a,self.b+o.b
    
obj1=operator_overloading(1,3)
obj2=operator_overloading(4,5)
obj3=obj2+obj1
print(obj3)