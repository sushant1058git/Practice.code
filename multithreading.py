# import threading
# print("CurrentExecutingThread:",threading.current_thread().getName())


'''Python Program to illustrate multithreading'''

# from threading import *


# def cube(num):
#     for i in range(8):
#         print("cube= "+str(num*num*num))
    
# def square(num1):
#     print("Square= "+str(num1*num1))
    

# t1=Thread(target=cube, args={10})
# t2=Thread(target=square, args={10})

# t1.start()
# t2.start()
# print("bye", current_thread().getName())


# # Python program to illustrate the concept of threading
# # importing the threading module
# import threading

# def print_cube(num):
# 	"""
# 	function to print cube of given num
# 	"""
# 	print("Cube: {}".format(num * num * num))

# def print_square(num):
# 	"""
# 	function to print square of given num
# 	"""
# 	print("Square: {}".format(num * num))

# if __name__ == "__main__":
# 	# creating thread
# 	t1 = threading.Thread(target=print_square, args=(10,))
# 	t2 = threading.Thread(target=print_cube, args=(10,))

# 	# starting thread 1
# 	t1.start()
# 	# starting thread 2
# 	t2.start()

# 	# wait until thread 1 is completely executed
# 	t1.join()
# 	# wait until thread 2 is completely executed
# 	t2.join()

# 	# both threads completely executed
# 	print("Done!")


    # # Python program to illustrate the concept of threading
    # import threading
    # import os

    # def task1():
    # 	print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    # 	print("ID of process running task 1: {}".format(os.getpid()))

    # def task2():
    # 	print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    # 	print("ID of process running task 2: {}".format(os.getpid()))

    # if __name__ == "__main__":

    # 	# print ID of current process
    # 	print("ID of process running main program: {}".format(os.getpid()))

    # 	# print name of main thread
    # 	print("Main thread name: {}".format(threading.current_thread().name))

    # 	# creating threads
    # 	t1 = threading.Thread(target=task1, name='t1')
    # 	t2 = threading.Thread(target=task2, name='t2')

    # 	# starting threads
    # 	t1.start()
    # 	t2.start()

    # 	# wait until all threads finish
    # 	t1.join()
    # 	t2.join()


# '''Creating a thread by extending Thread Class'''
# from threading import *

# class sum(Thread):
#     def run(self):
#         for i in range(11):
#             print(i, current_thread().name)
        

# s=sum()
# s.start()
# s.join()
# print("Execution done",current_thread().name)


# '''Creating a thread without extending Thread Class'''

# from threading import *

# class sum():
#     def display(self):
#         for i in range(11):
#             print(i, current_thread().name)
        

# s=sum()
# t=Thread(target=s.display)
# t.start()
# t.join()
# print("Execution done",current_thread().name)


# '''Program to understand race condition in threading'''

# import threading

# x=0

# def increment():
#     global x
#     x += 1

# def thread_task():
#     for _ in range(100000):
#         increment() 
        
# def main_task():
#     global x
#     x=0
#     t1=threading.Thread(target=thread_task)
#     t2=threading.Thread(target=thread_task)
    
#     t1.start()
#     t2.start()
    
# if __name__ == "__main__":
#     for i in range(10):
#         main_task()
#         print("Iteration {0}: x = {1}".format(i,x))   


# '''Program to understand RLock () '''
# from threading import *

# class Flight:
#     def __init__(self,availbale_seat):
#         self.available_seat=availbale_seat
#         self.i=RLock()
#         print(self.i)
    
#     def reserve(self,seat_needed):
#         self.i.acquire()
#         print(self.i)
#         self.seat_needed=seat_needed
#         print(f"Available seat : {self.available_seat} ")
#         if self.available_seat >= self.seat_needed:
#             name=current_thread().name
#             print(f"{seat_needed} is alloted to {name}")
#             self.available_seat -= seat_needed
            
#         else:
#             print("No seats available")
#         self.i.release()
#         print(self.i)
            
# f=Flight(1)
# t1=Thread(target=f.reserve, args=(1,), name='Sushant')
# t2=Thread(target=f.reserve,args=(1,), name='Raj')

# t1.start()
# t2.start()


'''Program to understand Semaphore () '''
from threading import *

class Flight:
    def __init__(self,availbale_seat):
        self.available_seat=availbale_seat
        self.i=Semaphore(2)
        print(self.i)
    
    def reserve(self,seat_needed):
        self.i.acquire()
        print(self.i)
        self.seat_needed=seat_needed
        print(f"Available seat : {self.available_seat} ")
        if self.available_seat >= self.seat_needed:
            name=current_thread().name
            print(f"{seat_needed} is alloted to {name}")
            self.available_seat -= seat_needed
            
        else:
            print("No seats available")
        self.i.release()
        print(self.i)
            
f=Flight(3)
t1=Thread(target=f.reserve, args=(1,), name='Sushant')
t2=Thread(target=f.reserve,args=(1,), name='Raj')
t3=Thread(target=f.reserve,args=(1,), name='Naj')
t4=Thread(target=f.reserve,args=(1,), name='Baaj')

t1.start()
t2.start()
t3.start()
t4.start()

        