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


# '''Inheritance in Python'''

# # A Python program to demonstrate inheritance

# # Base or Super class. Note object in bracket.
# # (Generally, object is made ancestor of all classes)
# class Person(object):  #It is equivalent to class Person:
	
# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name

# 	# To check if this person is an employee
# 	def isEmployee(self):
# 		return False


# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):

# 	# Here we return true
# 	def isEmployee(self):
# 		return True

# # Driver code
# emp = Person("Geek1") # An Object of Person
# print(emp.getName(), emp.isEmployee())

# emp = Employee("Geek2") # An Object of Employee
# print(emp.getName(), emp.isEmployee())


# '''Python code to demonstrate how parent constructors are called.'''

# # parent class
# class Person( object ):	

# 		# __init__ is known as the constructor		
# 		def __init__(self, name, idnumber):
# 				self.name = name
# 				self.idnumber = idnumber
# 		def display(self):
# 				print(self.name)
# 				print(self.idnumber)

# # child class
# class Employee( Person ):		
# 		def __init__(self, name, idnumber, salary, post):
# 				self.salary = salary
# 				self.post = post

# 				# invoking the __init__ of the parent class
# 				Person.__init__(self, name, idnumber)

				
# # creation of an object variable or an instance
# a = Employee('Rahul', 886012, 200000, "Intern")	

# # calling a function of the class Person using its instance
# a.display()


# '''Python program to demonstrate error if we forget to invoke __init__() of the parent.'''

# class A:
# 	def __init__(self, n = 'Rahul'):
# 			self.name = n
# class B(A):
# 	def __init__(self, roll):
# 		    self.roll = roll
#             # A.__init__(self)

# object1 = B(23)
# print (object1.name)



# '''Python example to show the working of multiple inheritance'''
# class Base1(object):
# 	def __init__(self):
# 		self.str1 = "Geek1"
# 		print("Base1")

# class Base2(object):
# 	def __init__(self):
# 		self.str2 = "Geek2"		
# 		print("Base2")

# class Derived(Base1, Base2):
# 	def __init__(self):
		
# 		# Calling constructors of Base1 and Base2 classes
# 		Base1.__init__(self)
# 		Base2.__init__(self)
# 		print("Derived")
		
# 	def printStrs(self):
# 		print(self.str1, self.str2)
		

# ob = Derived()
# ob.printStrs()


# '''Example of multilevel Inheritance in Python'''

# class Parent:
#     def __init__(self, name):
#         self.name=name
#     def getName(self):
#         return self.name
    
# class Child(Parent):
#     def __init__(self, age):
#         super().__init__('Ram')
#         self.age=age
#     def getAge(self):
#         return self.age
    
# class grandChild(Child):
#     def __init__(self, bloodgroup):
#         super().__init__('28')
#         self.bloodgroup=bloodgroup
#     def getbloodGroup(self):
#         return self.bloodgroup


# obj=grandChild('B+')
# print(obj.getbloodGroup(), obj.getName(), obj.getAge())

# '''Private members of Parent class'''

# # Python program to demonstrate private members of the parent class
# class C(object):
# 	def __init__(self):
# 			self.c = 21

# 			# d is private instance variable
# 			self.__d = 42	
# class D(C):
# 	def __init__(self):
# 			self.e = 84
# 			C.__init__(self)
# object1 = D()

# # produces an error as d is private instance variable
# print(object1.d)

					
''' Python program to demonstrate protected members'''


# # Creating a base class
# class Base:
# 	def __init__(self):
# 		self._a = 2     # Protected member


# class Derived(Base):    # Creating a derived class
# 	def __init__(self):
# 		Base.__init__(self) # Calling constructor of Base class
# 		print("Calling protected member of base class: ")
# 		print(self._a)

# obj1 = Derived()
# obj2 = Base()

# print(obj2.a) # Calling protected member Outside class will result in AttributeError




'''Abstract class'''

# from abc import ABC, abstractmethod

# class mobile(ABC):
#     @abstractmethod
#     def model(self): #Abstract Method
#         pass
#     def ram(self, name):  #Concrete Method
#         return self.name


''' Python program showing abstract base class work'''
from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

        