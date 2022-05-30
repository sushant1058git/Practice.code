l=[5,8,45,65,878,34,67,4,0]

def Biggest_number(l):
    biggest_no=l[0]
    for item in l:
        if item>biggest_no:
            biggest_no=item
            
    print(biggest_no)
    
Biggest_number(l)