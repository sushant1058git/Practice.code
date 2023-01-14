# Find runtime of the following code

from random import randrange


def foo(array):
    sum=0
    product=0
    
    for i in array:
        sum += i
        
    for i in array:
        product *= i
        
    print("Sum :" +sum , "Product= " + product)
    
    
    
def printPairs(array):
    for i in array:
        for j in array:
            print(str(i), str(j))
            
            
def printUnorderedPairs(arrayA,arrayB):
    for i in range(arrayA):
        for j in range(arrayB):
            if arrayA[i] < arrayB[i]:
                print(str(arrayA[i])+str(arrayB[j]))
                

def printUnorderedPairs(arrayA,arrayB):
    for i in range(arrayA):
        for j in range(arrayB):
            for k in range(0,100000):
                    print(str(arrayA[i])+str(arrayB[j]))
                    
                    
 
                    
                    
