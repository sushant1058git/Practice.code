
A=[11,4,12,7]

def findMaxNumRec(A,n):
    if n==1:
        return A[0]
    return max(A(n-1),findMaxNumRec(A,n-1))


findMaxNumRec(A,4)