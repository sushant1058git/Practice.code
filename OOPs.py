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

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
        
#     def __add__(self,o):
#         return self.a+o.a,self.b+o.b
    
# obj1=A(1,3)
# obj2=A(4,5)
# obj3=obj2+obj1     #Equivalent to A.__add__(obj1,obj2)
# print(obj3)

# '''Method overloading'''
# class A:
#     def sum(self,a):
#         return a
#     def sum(self,a,b):
#         return a+b

# obj1=A()



# print(obj1.sum(10,20))
# print(obj1.sum(10))


# '''Method overloading using default arguments'''
# class add:
#     def sum(self,a=0,b=0,c=0):
#         if a!=0 and b!=0 and c!=0:
#             sum=a+b+c
#         elif a!=0 and b!=0 and c==0:
#             sum=a*b
#         elif a!=0 and b==0 and c==0:
#             sum=a
            
#         return sum
    
# obj=add()
# res=obj.sum(10,20,30)
# print(res)

# res=obj.sum(10,20)
# print(res)

# res=obj.sum(10)
# print(res)


# '''Method overloading using variable number of arguments'''

# class sum:
#     def add(self, *args):
#         total=0
#         for items in args:
#             total += items
#         return total
    
# obj=sum()
# res=obj.add(10,20,30)
# print(res)


# from multipledispatch import dispatch

# #passing one parameter
# @dispatch(int,int)
# def product(first,second):
# 	result = first*second
# 	print(result);

# #passing two parameters
# @dispatch(int,int,int)
# def product(first,second,third):
# 	result = first * second * third
# 	print(result);

# #you can also pass data type of any value as per requirement
# @dispatch(float,float,float)
# def product(first,second,third):
# 	result = first * second * third
# 	print(result);


# #calling product method with 2 arguments
# product(2,3,2) #this will give output of 12
# product(2.2,3.4,2.3) # this will give output of 17.985999999999997

# class Test:
#     def __init__(self):
#         print('No-Arg Constructor')

#     def __init__(self,a):
#         print('One-Arg constructor')

#     def __init__(self,a,b):
#         print('Two-Arg constructor')    #Only last constructor will be considered
# #t1=Test()
# #t1=Test(10)
# t1=Test(10,20)


# '''Method Overriding'''

# class Animal:
#     def move(self):
#         print("Animal is moving fast")
#     def eat(self):     #This method will be inherited in Dof class also
#         print("Animal is eating")
    
# class Dog(Animal):
#     def move(self):
#         print("Dog is moving slowly")    #Overriding method
#     def bark(self):
#         print("Dog is barking")     #This method is only available to dog class
        
# a=Animal()
# d=Dog()

# d.move() #This method is overriding in Dog class
# d.eat()  #This will be inherited from Animal class
# d.bark() #This method is only for Dog(child) class 

# # Python program to demonstrate calling the parent's class method inside the overridden method

# class Parent():
	
# 	def show(self):
# 		print("Inside Parent")
		
# class Child(Parent):
	
# 	def show(self):
		
# 		Parent.show(self) # Calling the parent's class method
# 		print("Inside Child")
		
# # Driver's code
# obj = Child()
# obj.show()


# class Parent():
	
# 	def show(self):
# 		print("Inside Parent")
		
# class Child(Parent):
	
# 	def show(self):
		
# 		super().show() # Calling the parent's class method
# 		print("Inside Child")
		
# # Driver's code
# obj = Child()
# obj.show()


# '''Constructor overriding'''

# class Parent:
#     def __init__(self):
#         print("This is parent constructor")
        
# class Child(Parent):
#    pass
        
# c=Child()
