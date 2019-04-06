"""
li=[1,2,3,4,5,6,7,8,9]
for n in (li):
    print(n)
    print(bin(n)[2:])
    a=(4**n-2**(n+1)-1)
    print(bin(a)[2:])
    
#josephs number 
#left shift by 1 add 1
for n in li:
    print("n val",n)
    n1=n
    n1=(n1<<1)
    print("shift",n1)
    n1=n1+1 
    print(n1)
    
#number of diagonals for a n sided polygon: catalan numbers
#lucas theorm
#stable marriage problem refer book
"""
#stolen value problem masked way

li=[0,9,3,5,8,2,4,7]

val=[]

val[0]=0;

val[1]=li[1]  
#basic initialization

for i in range(len(li)):
    val[i]=max(val[i-1],val[i-2]+li[i])
    
print(val)
    
