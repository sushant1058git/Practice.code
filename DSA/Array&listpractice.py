#  Question 1:Find the missing number from myList

from math import prod


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def missing(list,n):
    sum1=n*(n+1)/2
    sum2=sum(list)
    print(sum1-sum2)
    
    
missing(mylist,100)


#method 2

for i in range(1,101):
    if i not in mylist:
        print(i)
        
#Q3.)Write a program to find all pairs of integers whose sum is equal to given number:

l=[2,6,9,11,3]
target=9

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==9:
            print(l[i],l[j])    
            
            
#Q4.)Find max product of two intergers in array where all numbers of array are positive

l=[45,56,2,47,91,34]

def maxProd(l):
    product=1
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                continue
            elif l[i]*l[j]>product:
                product=l[i]*l[j]
    
    print(product)
    
maxProd(l)


#Q5)Implement an algorithm to check if a list has all unique numbers 

myList =[1, 20,21,44,21,34,56,21,34]

def isUnique(l):
    count=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                count+=1
                
    if count>1:
        print(f"All element are not unique {count}")
    else:
        print('Unique')
        
isUnique(myList)


myList =[1, 20,21,44,21,34,56,21,34]

def isUnique(l):
    count=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                count+=1
                
    if count>1:
        return False
    else:
        return True
        
print(isUnique(myList))


import numpy as np

arr=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])

#Write a function that return all elements from a list except first and last elements

myList=[1,2,3,4]
l=[]

def middle(lst):
    new=myList[1:len(lst)-1:]
    print(new)
            
            
middle(myList)
            
#Given a 2D list calculate the sum of diagonal elements

import numpy as np

my2DList=[[1,2,3],[4,5,6],[7,8,9]]
print(len(my2DList))

def diaSum(lst):
    sum=0
    for i in range(len(lst)):
        sum += lst[i][i]
    return sum
    

print(diaSum(my2DList))


#Write a function to find duplicate numbers on a given list

myList=[1,1,2,2,3,4,5]
l=[]

for i in myList:
    if i in l:
        pass
    else:
        l.append(i)
        
print(l)





        